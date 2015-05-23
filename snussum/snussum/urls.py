from django.conf.urls import include, url
from django.contrib import admin

from snussum.views import Home, Dashboard, About
from snussum.views.rules import Privacy, Service

from relationships.views.dating import DatingDetail, TodayDetail, DatingAccept, DatingRefuse, DatingRatingCreate
from relationships.views.self_dating import SelfDatingCreate, SelfDatingDetail, \
    SelfDatingApplyCreate, SelfDatingApplyAccept, SelfDatingApplyRefuse, \
    SelfDatingList

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Django Default
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^%s/' % settings.ADMIN_URL, include(admin.site.urls)),

    # Project Libraries
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^summernote/', include('django_summernote.urls')),

    # Project Urls
    url(r'^$', Home.as_view(), name='home'),
    url(r'^about/$', About.as_view(), name='about'),

    url(r'^rules/service/$', Service.as_view(), name='rule-service'),
    url(r'^rules/privacy/$', Privacy.as_view(), name='rule-privacy'),

    url(r'^today/$', Dashboard.as_view(), name='dashboard'),
    url(r'^ssum/(?P<slug>\w+)/$', DatingDetail.as_view(), name='dating-detail'),
    url(r'^ssum/(?P<slug>\w+)/accept/$', DatingAccept.as_view(), name='dating-accept'),
    url(r'^ssum/(?P<slug>\w+)/refuse/$', DatingRefuse.as_view(), name='dating-refuse'),
    url(r'^ssum/(?P<slug>\w+)/rating/$', DatingRatingCreate.as_view(), name='dating-rating'),

    url(r'^wanted/$', SelfDatingList.as_view(), name='self-dating-list'),
    url(r'^wanted/new/$', SelfDatingCreate.as_view(), name='self-dating-new'),
    url(r'^wanted/(?P<slug>\w+)/$', SelfDatingDetail.as_view(), name='self-dating-detail'),
    url(r'^wanted/(?P<slug>\w+)/apply/$', SelfDatingApplyCreate.as_view(), name='self-dating-apply'),

    url(r'^wanted/(?P<slug>\w+)/apply/(?P<self_dating_apply_hash_id>\w+)/accept/$',
        SelfDatingApplyAccept.as_view(),
        name='self-dating-apply-accept'),
    url(r'^wanted/(?P<slug>\w+)/apply/(?P<self_dating_apply_hash_id>\w+)/refuse/$',
        SelfDatingApplyRefuse.as_view(),
        name='self-dating-apply-refuse'),

    url(r'^', include('users.urls', namespace='users')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^snusex/', include('snusex.urls', namespace='snusex')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
