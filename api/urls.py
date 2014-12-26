from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
                        url(r'^api-login/', include('rest_framework.urls', namespace='rest_framework')), # User accessible
                        url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
                        url(r'^api/kits/$', views.KitList.as_view()), # User accessible
                        url(r'^api/kits/(?P<pk>[0-9]+)/$', views.KitDetail.as_view()),
                        url(r'^api/samples/$', views.SampleDemoList.as_view()), # User accessible
                        url(r'^api/samples/(?P<pk>[0-9]+)/$', views.SampleDemoDetail.as_view()), # User accessible
                        url(r'^api/samples/endproducts/$', views.SampleList.as_view()),
                        url(r'^api/samples/endproducts/(?P<pk>[0-9]+)/$', views.SampleDetail.as_view()),
                        url(r'^api/ckits/$', views.CustomKitList.as_view()),
                        url(r'^api/ckits/(?P<pk>[0-9]+)/$', views.CustomKitDetail.as_view()), # Only User accessible
                        url(r'^api/ckits/create/$', views.CustomKitCreate.as_view()), # User accessible
                        url(r'^api/users/$', views.UserList.as_view()),
                        url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()), # User accessible
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
