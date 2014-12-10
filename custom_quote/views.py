from django.shortcuts import render_to_response
from django.views.generic.base import View
# Create your views here.


class CustomQuote(View):
    # Main Kit builder AngularJS/Ember App
    def get(self, request):
        return render_to_response('CustomQuote/custom_quote.html')

