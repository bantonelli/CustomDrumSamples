__author__ = 'brandonantonelli'

from rest_framework import serializers
from kitbuilder.models import Sale, Tag, KitDescription, Kit, Sample, CustomKit


class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = ('name', 'demo', 'wav', 'kit', 'type')


class KitSerializer(serializers.ModelSerializer):

    samples = SampleSerializer(many=True, read_only=True)

    class Meta:
        model = Kit
        fields = ('name', 'new', 'on_sale', 'soundcloud', 'image', 'tags', 'description', 'price', 'sale', 'user_rating', 'samples')


class CustomKitSerializer(serializers.ModelSerializer):

    samples = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = CustomKit
        fields = ('name', 'user', 'date', 'samples')

