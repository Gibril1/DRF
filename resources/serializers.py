from rest_framework import serializers
from .models import Resource, AdditionalResource

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class AdditionalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalResource
        fields = '__all__'