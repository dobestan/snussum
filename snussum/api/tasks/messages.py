from celery import shared_task

from snussum.settings import MAILGUN_SERVER_NAME, MAILGUN_ACCESS_KEY
from snussum.settings import API_STORE_SMS_KEY, API_STORE_SMS_BASE_URL
from snussum.settings import API_STORE_SMS_SEND_NAME, API_STORE_SMS_SUBJECT

from django.conf import settings

from api.tasks.shortener import shorten_url
import requests

import logging


logger = logging.getLogger(__name__)


@shared_task
def send_sms(data, url=None):
    """
    data = {
        'to': "...", ( * required )
        'body': "...", ( * required )
    }
    """

    headers = {
        'x-waple-authorization': API_STORE_SMS_KEY
    }

    data['dest_phone'] = data['to']
    data['msg_body'] = data['body']

    if url:
        url = shorten_url(url)
        data['msg_body'] = data['body'] + " " + url

    data['send_phone'] = data['dest_phone']
    data['send_name'] = API_STORE_SMS_SEND_NAME
    data['subject'] = API_STORE_SMS_SUBJECT

    if settings.DEBUG:
        logger.debug('Send SMS | %s' % (data))
        return True

    request = requests.post(
        API_STORE_SMS_BASE_URL,
        data=data,
        headers=headers,
    )
    return request


@shared_task
def send_email(data, url=None):
    """
    data = {
        'to': "...", ( * required )
        'subject': "...", ( * required )
        'body': "...", ( * required )
    }
    """

    MAILGUN_EMAIL_BASE_URL = "https://api.mailgun.net/v3/%s/messages" % MAILGUN_SERVER_NAME
    MAILGUN_AUTHENTICATION_DATA = ('api', MAILGUN_ACCESS_KEY)

    data['from'] = '스누썸 <contact@snussum.com>'
    data['text'] = data['body']

    if url:
        url = shorten_url(url)
        data['text'] = data['body'] + " " + url

    request = requests.post(
        MAILGUN_EMAIL_BASE_URL,
        auth=MAILGUN_AUTHENTICATION_DATA,
        data=data,
    )
    return request
