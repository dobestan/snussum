from django.conf.urls import include, url
from django.contrib import admin

from snussum.views import Home, Dashboard, DatingDetail, TodayDetail

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Django Default
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Project Libraries
    url('', include('social.apps.django_app.urls', namespace='social')),


    # Project Urls
    url(r'^$', Home.as_view(), name='home'),
    url(r'^ssum/$', Dashboard.as_view(), name='dashboard'),

    url(r'^ssum/(?P<slug>\w+)/$', DatingDetail.as_view(), name='dating-detail'),
    url(r'^today/$', TodayDetail.as_view(), name='today'),

    url(r'^', include('users.urls', namespace='users')),
    url(r'^api/', include('api.urls', namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
