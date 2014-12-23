from serializers import *
from rest_framework import generics, permissions
from api.permissions import IsKitOwner, IsUser


########### API VIEWS
#SOUND SAMPLE
class SampleList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleDemoList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Sample.objects.all()
    serializer_class = SampleDemoSerializer


class SampleDemoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Sample.objects.all()
    serializer_class = SampleDemoSerializer

#SAMPLE KIT
class KitList(generics.ListAPIView):
    """
    List all Drum Kits
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Kit.objects.all()
    serializer_class = KitSerializerLimited


class KitDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Kit.objects.all()
    serializer_class = KitSerializerFull


#CUSTOM KIT
class CustomKitList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = CustomKit.objects.all()
    serializer_class = CustomKitSerializer


class CustomKitDetail(generics.RetrieveDestroyAPIView):
    # Make Custom permission so that it checks if is authenticated and is user that created kit
    permission_classes = (permissions.IsAuthenticated, IsKitOwner)
    queryset = CustomKit.objects.all()
    serializer_class = CustomKitPurchasedSerializer


class CustomKitCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CustomKitSerializerCreate


#USER
class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer(read_only=True)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    # Make Custom permission so that it checks if is authenticated and is user that owns profile.
    permission_classes = (permissions.IsAuthenticated, IsUser)
    queryset = User.objects.all()
    serializer_class = UserSerializer
