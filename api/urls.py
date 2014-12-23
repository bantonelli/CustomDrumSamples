from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
                        url(r'^api/kits/$', views.KitList.as_view()),
                        url(r'^api/kits/(?P<pk>[0-9]+)/$', views.KitDetail.as_view()),
                        url(r'^api/samples/$', views.SampleList.as_view()),
                        url(r'^api/samples/(?P<pk>[0-9]+)/$', views.SampleDetail.as_view()),
                        url(r'^api/ckits/$', views.CustomKitList.as_view()),
                        url(r'^api/ckits/(?P<pk>[0-9]+)/$', views.CustomKitDetail.as_view()),
                        url(r'^api/users/$', views.UserList.as_view()),
                        url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
                        url(r'^api/users/profiles/$', views.UserProfileList.as_view()),
                        url(r'^api/users/(?P<pk>[0-9]+)/profiles/$', views.UserProfileDetail.as_view()),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
