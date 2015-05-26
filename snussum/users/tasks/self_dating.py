from celery import shared_task
from api.tasks.messages import send_sms
from api.tasks.shortener import url_builder


def send_self_dating_applied_sms(user, partner, self_dating_apply):
    UTM_SOURCE = "sms"
    UTM_MEDIUM = "self_dating_applied"

    url = url_builder(self_dating_apply.get_full_absolute_url(), utm_source=UTM_SOURCE, utm_medium=UTM_MEDIUM)

    data = {
        'to': user.userprofile.phonenumber,
        'body': "[스누썸] %s님이 셀프소개팅에 지원하였습니다." % (partner.userprofile.nickname),
    }

    send_sms.delay(data, url)
