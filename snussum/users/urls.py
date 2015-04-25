from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',

    url(r'^login/$', 'users.views.login', name='login'),
)
