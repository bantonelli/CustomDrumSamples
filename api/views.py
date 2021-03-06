from django.shortcuts import render_to_response
from django.views.generic.base import View
from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, HttpResponse
import urllib
import urllib2

from serializers import *
from rest_framework import generics, permissions
from api.permissions import IsKitOwner, IsUser
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

########### API VIEWS


#Authorization


# Might Have to change this to use the JSON Response from rest framework
class LogInView(View):

    # Have to use the ensure_csrf_cookie decorator on view because form is generated by angular
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(LogInView, self).dispatch(*args, **kwargs)

# Kit Builder Client ID = aR!omYsELvz.Jihdlfk-xUdkPpZ2f7qc9L415fV2
# Kit Builder Client Secret = U_qMHU-cWBD58vu5DOcp3U0RO79t5zEfIdoF1Xn.E:FT_ztn2WsdAxfV_V@V0Ji?Wb=IQl:1xM!X8WTb9kIH-!!uu1PUS0XVpYr6DxwXeEgJlUFBwpS7co8xtB9!5CAC
    def post(self, request):
        request.session["isloggedin"] = True
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        client_id = request.POST.get('client_id', '')
        url = 'http://127.0.0.1:8000/o/token/'
        if (client_id == "aR!omYsELvz.Jihdlfk-xUdkPpZ2f7qc9L415fV2"):
            client_secret = "U_qMHU-cWBD58vu5DOcp3U0RO79t5zEfIdoF1Xn.E:FT_ztn2WsdAxfV_V@V0Ji?Wb=IQl:1xM!X8WTb9kIH-!!uu1PUS0XVpYr6DxwXeEgJlUFBwpS7co8xtB9!5CAC"
        values = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'password',
            'username': username,
            'password': password
        }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        #Authentication step something like --> user = auth.authenticate(username=username, password=password)
        # Need to make this access the next value from Url and Redirect there if login was successful
        return HttpResponse(urllib2.urlopen(req))

#SOUND SAMPLE
class SampleList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser, TokenHasReadWriteScope)
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser, TokenHasReadWriteScope)
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleDemoList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, TokenHasScope)
    required_scopes = ['read']
    queryset = Sample.objects.all()
    serializer_class = SampleDemoSerializer


class SampleDemoDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, TokenHasScope)
    required_scopes = ['read']
    queryset = Sample.objects.all()
    serializer_class = SampleDemoSerializer

#SAMPLE KIT
class KitList(generics.ListAPIView):
    """
    List all Drum Kits
    """
    permission_classes = (permissions.IsAuthenticated, TokenHasScope)
    required_scopes = ['read']
    queryset = Kit.objects.all()
    serializer_class = KitSerializerLimited


class KitDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser, TokenHasReadWriteScope)
    queryset = Kit.objects.all()
    serializer_class = KitSerializerFull


#CUSTOM KIT
class CustomKitList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser, TokenHasReadWriteScope)
    queryset = CustomKit.objects.all()
    serializer_class = CustomKitSerializer


class CustomKitDetail(generics.RetrieveDestroyAPIView):
    # Make Custom permission so that it checks if is authenticated and is user that created kit
    permission_classes = (permissions.IsAuthenticated, IsKitOwner, TokenHasScope)
    required_scopes = ['read']
    queryset = CustomKit.objects.all()
    serializer_class = CustomKitPurchasedSerializer


class CustomKitCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, TokenHasReadWriteScope)
    serializer_class = CustomKitSerializerCreate


#USER
class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser, TokenHasScope)
    required_scopes = ['read']
    queryset = User.objects.all()
    serializer_class = UserSerializer(read_only=True)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    # Make Custom permission so that it checks if is authenticated and is user that owns profile.
    permission_classes = (permissions.IsAuthenticated, IsUser, TokenHasReadWriteScope)
    queryset = User.objects.all()
    serializer_class = UserSerializer
