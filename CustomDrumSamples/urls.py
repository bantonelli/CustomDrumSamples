from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CustomDrumSamples.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('kitbuilder.urls')),

    # Main Site Navigation
    url(r'^$', views.LandingPage.as_view()),
    url(r'^about/$', views.AboutUs.as_view()),
    url(r'^team/$', views.TeamProfile.as_view()),
    url(r'^legal/$', views.Legal.as_view()),
    url(r'^contact/$', views.Contact.as_view()),
    url(r'^colorway/$', views.ResponsiveSiteColorway.as_view()),


)
