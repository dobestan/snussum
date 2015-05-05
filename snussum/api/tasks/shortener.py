from celery import shared_task

from snussum.settings import GOOGLE_API_KEY

import urllib
import requests
import json



@shared_task
def shorten_url(long_url):
    """
    Generate shorten URL via goo.gl api
    - https://developers.google.com/url-shortener/v1/getting_started
    """

    BASE_URL = "https://www.googleapis.com/urlshortener/v1/url"
    params = {
        'key': GOOGLE_API_KEY,
    }
    headers = {'Content-Type': 'application/json'}
    data = {
        'longUrl': long_url
    }

    response = requests.post(BASE_URL, params=params, data=json.dumps(data), headers=headers)
    return response


def url_builder(url, utm_source=None, utm_medium=None, utm_term=None, utm_content=None, utm_campaign=None):
    """
    URL Builder for Google Analytics
    - https://support.google.com/analytics/answer/1033867?hl=en
    """

    data = {}
    if utm_source: data['utm_source'] = utm_source
    if utm_medium: data['utm_medium'] = utm_medium
    if utm_term: data['utm_term'] = utm_term
    if utm_content: data['utm_content'] = utm_content
    if utm_campaign: data['utm_campaign'] = utm_campaign

    return url + "?" + urllib.parse.urlencode(data)
