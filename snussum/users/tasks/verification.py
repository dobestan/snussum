from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from django.template.loader import get_template
from django.template import Context

from api.tasks.messages import send_email, send_sms
from api.tasks.shortener import shorten_url, url_builder

from selenium import webdriver

from snussum.settings import SNUSSUM_URL
from api.tasks.shortener import url_builder


def send_phonenumber_verification_sms(user):
    UTM_SOURCE = "sms"
    UTM_MEDIUM = "phonenumber_verification"

    url = reverse(
        "users:phonenumber-verification",
        kwargs={
            'phonenumber_verification_token': user.userprofile.phonenumber_verification_token})

    url = url_builder(SNUSSUM_URL + url, utm_source=UTM_SOURCE, utm_medium=UTM_MEDIUM)

    data = {
        'to': user.userprofile.phonenumber,
        'body': "[스누썸] 링크를 클릭하시면 휴대폰 인증이 완료됩니다.",
    }

    send_sms.delay(data, url)


def send_university_verification_email(user):
    UTM_SOURCE = "email"
    UTM_MEDIUM = "mysnu_verification"

    email_template = get_template("users/email/university_verification.html")
    email_context = Context({
        'username': user.username,
    })

    url = SNUSSUM_URL + reverse('users:university-verification',
                                kwargs={'university_verification_token': user.userprofile.university_verification_token,
                                        })
    url = url_builder(url, utm_source=UTM_SOURCE, utm_medium=UTM_MEDIUM)

    data = {
        'to': "dobestan@gmail.com",
        'subject': "[스누썸] 서울대학교 동문 인증 이메일",
        'body': email_template.render(email_context),
    }

    send_email.delay(data, url)


def snulife_login(username, password):
    """
    서울대학교 커뮤니티, 스누라이프에 접속해서 이용자가 입력한 아이디, 비밀번호로
    실제로 로그인이 되는지 체크하고 결과를 Boolean으로 리턴한다.

    - 스누라이프 : http://snulife.com/
    - 스누라이프 로그인 : https://snulife.com/?act=dispMemberLoginForm
    - 스누라이프 마이페이지 : https://snulife.com/index.php?&act=dispMemberInfo
    """
    BASE_URL = "https://snulife.com"
    LOGIN_URL = "https://snulife.com/?act=dispMemberLoginForm"
    MYPAGE_URL = "https://snulife.com/index.php?&act=dispMemberInfo"

    driver = webdriver.PhantomJS()

    # 로그인 진행
    driver.get(LOGIN_URL)

    input_username = driver.find_element_by_id("uid")
    input_username.send_keys(username)

    input_password = driver.find_element_by_id("upw")
    input_password.send_keys(password)

    login_button = driver.find_element_by_css_selector("div#content div.btnArea span.btn input")
    login_button.click()

    # 마이페이지 검증
    # 스누라이프의 경우에는 마이페이지에서 검증하지 않고,
    # 메인 페이지에서 닉네임이 있는지 살펴보고 검증한다

    driver.get(BASE_URL)
    username_element = driver.find_elements_by_css_selector("div.default_login div.userNickName span")
    username = username_element[0] if username_element else None

    # snulife_username.get_attribute('innerHTML'))

    driver.quit()

    if username:
        return True
    return False


def mysnu_login(username, password):
    """
    서울대학교 공식 포털, 마이스누에 접속해서 이용자가 입력한 아이디, 비밀번호로
    실제로 로그인이 되는지 체크하고 결과를 Boolean으로 리턴한다.

    - 마이스누 : http://my.snu.ac.kr/mysnu/portal/
    - 마이스누 마이페이지 :
    """

    BASE_URL = "http://my.snu.ac.kr/mysnu/portal/"

    driver = webdriver.PhantomJS()

    # 로그인 진행
    # 마이스누의 경우에는 별도의 로그인 페이지 없이 메인페이지에서 바로 접속

    driver.get(BASE_URL)

    input_username = driver.find_element_by_id("si_id")
    input_username.send_keys(username)

    input_password = driver.find_element_by_id("si_pwd")
    input_password.send_keys(password)

    login_button = driver.find_element_by_id("btn_login")
    login_button.click()

    # 로그인 검증
    # 마이스누의 경우에는 iFrame, Frameset을 이용한 방식을 차용하고 있어
    # Selenium으로 특정 Element를 가져오는 것이 힘들다.

    # if Login fails
    # - https://sso.snu.ac.kr/nls3/error.jsp?errorCode=5401

    current_url = driver.current_url
    driver.quit()

    if "nls" in current_url:
        return False
    return True
