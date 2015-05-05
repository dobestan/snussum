from celery import shared_task

from snussum.settings import GOOGLE_API_KEY
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
