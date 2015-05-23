from django.conf.urls import patterns, url

from snusex.views import About


urlpatterns = patterns(
    '',
    url(r'^about/$', About.as_view(), name='about'),
)
