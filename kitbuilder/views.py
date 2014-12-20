from django.shortcuts import render_to_response
from django.views.generic.base import View
# Create your views here.


class KitBuilder(View):
    # Main Kit builder AngularJS/Ember App
    def get(self, request):
        li_list = [x for x in range(40)]
        li_list2 = [x for x in range(10)]
        section_list = [x for x in range(7)]
        tags = ["Ambient", "Hard", "Gritty", "Tyson"]
        return render_to_response('KitBuilder/kitbuilder.html', locals())

