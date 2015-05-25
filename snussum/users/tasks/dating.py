from celery import shared_task
from api.tasks.messages import send_sms
from api.tasks.shortener import url_builder


def send_dating_matched_sms(user, partner, dating):
    UTM_SOURCE = "sms"
    UTM_MEDIUM = "dating_matched"

    if user.userprofile.is_phonenumber_verified:
        url = url_builder(dating.get_full_absolute_url(), utm_source="sms", utm_medium="dating_matched")

        data = {
            'to': user.userprofile.phonenumber,
            'body': "[스누썸] %s님과 새롭게 매칭되었습니다. %s" % (partner.userprofile.nickname),
        }

        send_sms.delay(data, url)


def send_dating_accepted_sms(user, partner):
    UTM_SOURCE = "sms"
    UTM_MEDIUM = "dating_accepted"


def send_dating_refused_sms(user, partner):
    UTM_SOURCE = "sms"
    UTM_MEDIUM = "dating_refused"
