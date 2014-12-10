__author__ = 'brandonantonelli'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^custom-quote/$', views.CustomQuote.as_view()),
                       url(r'^customquote/$', views.CustomQuote.as_view()),
                       )