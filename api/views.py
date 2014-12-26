from serializers import *
from rest_framework import generics, permissions
from api.permissions import IsKitOwner, IsUser
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


########### API VIEWS
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
