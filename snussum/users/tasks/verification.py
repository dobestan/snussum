from celery import shared_task

from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from django.template.loader import get_template
from django.template import Context

from api.tasks.messages import send_email, send_sms
from api.tasks.shortener import shorten_url, url_builder

from selenium import webdriver


@shared_task
def send_phonenumber_verification_sms(user_id):
    user = User.objects.get(pk=user_id)

    url = reverse(
        "users:phonenumber-verification",
        kwargs={
            'phonenumber_verification_token': user.userprofile.phonenumber_verification_token})

    url = "http://local.snussum.com:9000" + url
    url = url_builder(url, utm_source="sms", utm_medium="verification")
    url = shorten_url(url)

    data = {
        'to': user.userprofile.phonenumber,
        'body': "[스누썸] 링크를 클릭하시면 인증이 완료됩니다. ( %s )" % url,
    }

    send_sms.delay(data)


def send_university_verification_email(user_id):
    user = User.objects.get(pk=user_id)

    email_template = get_template("users/email/university_verification.html")
    email_context = Context({
        'username': user.username,
        'verify': reverse('users:university-verification', kwargs={
            'university_verification_token': user.userprofile.university_verification_token,
        })
    })

    data = {
        'to': "dobestan@gmail.com",
        'subject': "[스누썸] 서울대학교 학생 인증을 위한 이메일입니다.",
        'body': email_template.render(email_context),
    }

    send_email.delay(data)


def snulife_login(username, password):
    BASE_URL = "https://snulife.com/?act=dispMemberLoginForm"

    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    input_username = driver.find_element_by_id("uid")
    input_username.send_keys(username)

    input_password = driver.find_element_by_id("upw")
    input_password.send_keys(password)

    login_button = driver.find_element_by_css_selector("div#content div.btnArea span.btn input")
    login_button.click()

    if driver.find_elements_by_css_selector("div.userNickName"):
        return True
    return False


def mysnu_login(username, password):
    BASE_URL = "http://my.snu.ac.kr/mysnu/portal/"

    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    input_username = driver.find_element_by_id("si_id")
    input_username.send_keys(username)

    input_password = driver.find_element_by_id("si_pwd")
    input_password.send_keys(password)

    login_button = driver.find_element_by_id("btn_login")
    login_button.click()

    # if Login fails
    # - https://sso.snu.ac.kr/nls3/error.jsp?errorCode=5401

    if "nls" in driver.current_url:
        return False
    return True
