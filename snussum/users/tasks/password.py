from django.contrib.auth.models import User

from django.template.loader import get_template
from django.template import Context

from api.tasks.messages import send_email, send_sms


def send_password_reset_email(user, password):
    if user.email:
        email_template = get_template("users/email/password_reset.html")
        email_context = Context({
            'username': user.username,
            'password': password,
        })

        data = {
            'to': user.email,
            'subject': "[스누썸] 비밀번호가 재설정되었습니다.",
            'body': email_template.render(email_context),
        }

        send_email.delay(data)


def send_password_reset_sms(user, password):
    if user.userprofile.is_phonenumber_verified:
        data = {
            'to': user.userprofile.phonenumber,
            'body': "[스누썸] 비밀번호가 재설정되었습니다. [비밀번호: %s]" % password,
        }

        send_sms.delay(data)
