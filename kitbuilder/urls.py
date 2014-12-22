from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
                       url(r'^kit-builder/$', views.KitBuilder.as_view()),
                       url(r'^kitbuilder/$', views.KitBuilder.as_view()),
                       url(r'^kits/$', views.KitList.as_view()),
                       url(r'^kits/(?P<pk>[0-9]+)/$', views.KitDetail.as_view()),
                       url(r'^samples/$', views.SampleList.as_view()),
                       url(r'^samples/(?P<pk>[0-9]+)/$', views.SampleDetail.as_view()),
                       url(r'^ckits/$', views.CustomKitList.as_view()),
                       url(r'^ckits/(?P<pk>[0-9]+)/$', views.CustomKitDetail.as_view())
                       )

urlpatterns = format_suffix_patterns(urlpatterns)

