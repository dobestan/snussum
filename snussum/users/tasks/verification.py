from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from django.template.loader import get_template
from django.template import Context

from api.tasks.messages import send_email

import requests


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
    BASE_URL = "http://snulife.com/main"

    data = {
            'success_return_url': '/main',
            'act': 'procMemberLogin',
            'mid': 'main',
            'user_id': username,
            'password': password,
    }

    response = requests.post(BASE_URL, data=data, params={}, headers={})

    if "잘못된 비밀번호입니다." in response.content.decode(response.encoding):
        return False
    return True
