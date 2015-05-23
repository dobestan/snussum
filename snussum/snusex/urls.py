from django.conf.urls import patterns, url

from snusex.views import Home, About


urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^about/$', About.as_view(), name='about'),
)
