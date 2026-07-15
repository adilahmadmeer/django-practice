from rest_framework import serializers
from .models import asset
class asset_serializer(serializers.ModelSerializer):
        id = serializers.IntegerField()
        mac = serializers.CharField(max_length=50)
        ip_address1 = serializers.CharField(max_length=50)
        class Meta:
            model = asset
            fields = [
                'id',
                'mac',
                'ip_address1'
            ]
        def validate(self, data):
            errors = {}
            for field in self.Meta.fields:
                value = data.get(field)
                if value in [None, ""]:
                    errors[field] = f"{field} is required."
            if errors:
                raise serializers.ValidationError(errors)
            return data