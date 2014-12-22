from django.shortcuts import render_to_response
from django.views.generic.base import View
# Create your views here.
from kitbuilder.models import Sale, Tag, KitDescription, Kit, Sample, CustomKit
from kitbuilder.serializers import KitSerializer, SampleSerializer, CustomKitSerializer
from rest_framework import generics


########### API VIEWS
#SOUND SAMPLE
class SampleList(generics.ListAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


#SAMPLE KIT
class KitList(generics.ListAPIView):
    """
    List all Drum Kits
    """
    queryset = Kit.objects.all()
    serializer_class = KitSerializer


class KitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer


#CUSTOM KIT
class CustomKitList(generics.ListCreateAPIView):
    queryset = CustomKit.objects.all()
    serializer_class = CustomKitSerializer


class CustomKitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomKit.objects.all()
    serializer_class = CustomKitSerializer


#FRONT END APP VIEW
class KitBuilder(View):
    # Main Kit builder AngularJS/Ember App
    def get(self, request):
        li_list = [x for x in range(40)]
        li_list2 = [x for x in range(10)]
        section_list = [x for x in range(7)]
        tags = ["Ambient", "Hard", "Gritty", "Tyson"]
        return render_to_response('KitBuilder/kitbuilder.html', locals())

