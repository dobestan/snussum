from celery import shared_task
from api.tasks.messages import send_sms


def send_dating_matched_sms(user, partner, dating):
    if user.userprofile.is_phonenumber_verified:
        data = {
            'to': user.userprofile.phonenumber,
            'body': "[스누썸] %s 님과 매칭되었습니다." % (partner.userprofile.nickname),
        }

        send_sms.delay(data)


def send_dating_accepted_sms(user, partner):
    pass

def send_dating_refused_sms(user, partner):
    pass
