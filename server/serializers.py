from .models import Amazon, Gevolution
from rest_framework import serializers

class AmazonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon
        fields = '__all__'

class GevolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gevolution
        fields = '__all__'
