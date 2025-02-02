from rest_framework import serializers
from .models import ImageModel

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['id', 'original_image', 'small_image', 'medium_image']
