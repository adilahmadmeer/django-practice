from rest_framework import serializers
from .models import asset
class asset_serializer(serializers.ModelSerializer):
         class Meta:
            model = asset
            fields = '__all__'
