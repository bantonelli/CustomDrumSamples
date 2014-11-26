from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^kit-builder/$', views.KitBuilder.as_view()),
                       )