from snussum.settings import MAILGUN_SERVER_NAME, MAILGUN_ACCESS_KEY

import requests


def send_email(data):
    """
    data should have 3 arguments
    data = {
        'to': "...",
        'subject': "...",
        'text': "...",
    }
    """

    MAILGUN_EMAIL_BASE_URL = "https://api.mailgun.net/v3/%s/messages" % MAILGUN_SERVER_NAME
    MAILGUN_AUTHENTICATION_DATA = ('api', MAILGUN_ACCESS_KEY)

    data['from'] = '스누썸 <contact@snussum.com>'
    data['to'] = 'dobestan@gmail.com'
    data['subject'] = 'hello world'
    data['text'] = 'hello world'

    request = requests.post(
        MAILGUN_EMAIL_BASE_URL,
        auth=MAILGUN_AUTHENTICATION_DATA,
        data=data,
    )
    return request
