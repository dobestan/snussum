from snussum.settings import API_STORE_SMS_KEY, API_STORE_SMS_BASE_URL
from snussum.settings import API_STORE_SMS_SEND_NAME, API_STORE_SMS_SUBJECT

import requests


def send_sms(data):
    """
    data should have 3 arguments
    data = {
        'dest_phone': "...",
        'msg_body': "...",
    }
    """
    headers = {
        'x-waple-authorization': API_STORE_SMS_KEY
    }

    data['send_phone'] = data['dest_phone']
    data['send_name'] = API_STORE_SMS_SEND_NAME
    data['subject'] = API_STORE_SMS_SUBJECT

    request = requests.post(
        API_STORE_SMS_BASE_URL,
        data=data,
        headers=headers,
    )
    return request
