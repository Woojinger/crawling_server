from .models import Amazon, Gevolution, Fiftytohundred
from rest_framework import serializers

class AmazonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon
        fields = '__all__'

class GevolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gevolution
        fields = '__all__'

class FiftytohundredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiftytohundred
        fields = '__all__'