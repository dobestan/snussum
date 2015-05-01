from snussum.settings import MAILGUN_SERVER_NAME, MAILGUN_ACCESS_KEY

import requests


def send_email(data):
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
    data['to'] = 'dobestan@gmail.com'
    data['text'] = data['body']

    request = requests.post(
        MAILGUN_EMAIL_BASE_URL,
        auth=MAILGUN_AUTHENTICATION_DATA,
        data=data,
    )
    return request
