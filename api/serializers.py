__author__ = 'brandonantonelli'

from rest_framework import serializers
from kitbuilder.models import Sale, Tag, KitDescription, Kit, Sample, CustomKit
from userprofile.models import UserProfile, User


# KIT BUILDER
class SampleDemoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = ('name', 'demo', 'kit', 'type')


class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = ('name', 'demo', 'wav', 'kit', 'type')


class KitDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = KitDescription
        fields = ('selling_point1', 'selling_point2', 'selling_point3', 'author', 'date_created')


class KitSerializerFull(serializers.ModelSerializer):
    samples = SampleSerializer(many=True, read_only=True)
    description = KitDescriptionSerializer(read_only=True)

    class Meta:
        model = Kit
        fields = ('name', 'new', 'on_sale', 'soundcloud', 'image', 'tags', 'description', 'price', 'sale', 'user_rating', 'samples')


class KitSerializerLimited(serializers.ModelSerializer):
    samples = SampleSerializer(many=True, read_only=True)
    #samples = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    description = KitDescriptionSerializer(read_only=True)

    class Meta:
        model = Kit
        fields = ('name', 'new', 'on_sale', 'soundcloud', 'image', 'tags', 'description', 'price', 'sale', 'user_rating', 'samples')


class CustomKitSerializer(serializers.ModelSerializer):
    samples = serializers.PrimaryKeyRelatedField(many=True)
    user = serializers.CharField(read_only=True, source='user.user.username')

    class Meta:
        model = CustomKit
        fields = ('name', 'user', 'date', 'samples')


class CustomKitPurchasedSerializer(serializers.ModelSerializer):
    samples = SampleSerializer(many=True, read_only=True)
    user = serializers.CharField(read_only=True, source='user.user.username')

    class Meta:
        model = CustomKit
        fields = ('name', 'user', 'date', 'samples')


class CustomKitSerializerCreate(serializers.ModelSerializer):
    samples = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomKit
        fields = ('name', 'date', 'user', 'samples')


# USER PROFILE
class UserProfileSerializer(serializers.ModelSerializer):
    custom_kits = CustomKitPurchasedSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'last_4_digits', 'created_at', 'updated_at', 'custom_kits')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'profile')