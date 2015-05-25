from celery import shared_task
from api.tasks.messages import send_sms
from api.tasks.shortener import shorten_url, url_builder


def send_dating_matched_sms(user, partner, dating):
    if user.userprofile.is_phonenumber_verified:
        url = url_builder("http://local.snussum.com:9000" + dating.get_absolute_url(), utm_source="sms", utm_medium="dating_matched")
        url = shorten_url(url)

        data = {
            'to': user.userprofile.phonenumber,
            'body': "[스누썸] %s님과 새롭게 매칭되었습니다. %s" % (partner.userprofile.nickname, url),
        }

        send_sms.delay(data)


def send_dating_accepted_sms(user, partner):
    pass

def send_dating_refused_sms(user, partner):
    pass
