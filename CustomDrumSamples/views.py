from django.shortcuts import render_to_response
from django.views.generic.base import View
# Create your views here.


class LandingPage(View):
    #fancy landing page
    def get(self, request):
        title = "Custom Drum Samples"
        return render_to_response('landingpage.html', locals())


class AboutUs(View):
    # mission statement, vision, what we do
    def get(self, request):
        return render_to_response('aboutus.html')


class TeamProfile(View):
    # People involved in business with pop-up profiles for each team member
    # Use the team member model which extends user
    def get(self, request):
        return render_to_response('teamprofile.html')


class Legal(View):

    #Privacy Policies
    #Terms of Usage
    def get(self, request):
        return render_to_response('legal.html')


class ResponsiveSiteColorway(View):

    def get(self, request):
        title = "Colorway for Custom Drum Samples"
        return render_to_response('colorway.html', locals())