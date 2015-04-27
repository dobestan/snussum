from django.conf.urls import include, url
from django.contrib import admin

from snussum.views import Home, Dashboard, DatingDetail


urlpatterns = [
    # Examples:
    # url(r'^$', 'snussum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Django Default
    url(r'^admin/', include(admin.site.urls)),

    # Project Libraries

    # Project Urls
    url(r'^$', Home.as_view(), name='home'),
    url(r'^ssum/$', Dashboard.as_view(), name='dashboard'),

    url(r'^ssum/(?P<slug>\w+)/$', DatingDetail.as_view(), name='dating-detail'),

    url(r'^', include('users.urls', namespace='users')),
]
