from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from django.contrib.auth.models import User

from django.template.loader import get_template
from django.template import Context


def send_university_verification_email(user_id):
    user = User.objects.get(pk=user_id)

    email_template = get_template("users/email/university_verification.html")
    email_context = Context({
        'username': user.username,
        'verify': reverse('users:university-verification', kwargs={
            'university_verification_token': user.userprofile.university_verification_token,
        })
    })

    send_mail(
        "[스누썸] 서울대학교 학생 인증을 위한 이메일입니다.",
        email_template.render(email_context),
        "스누썸 <verify@snussum.com>",
        ["dobestan@snu.ac.kr"],
        fail_silently=False,
    )
