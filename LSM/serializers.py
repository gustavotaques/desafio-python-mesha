from django.db.models import fields
from rest_framework import serializers
from .models import Obra
from rest_framework.exceptions import ValidationError

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        exclude = ['created_at']
    
    def validate_autores(self, data):
        if isinstance(data, list):
            return data
        raise ValidationError({"error": "O nome dos autores devem estar em uma lista"})
    
    def create(self, validated_data):
        return super().create(validated_data)


class ObraUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class SaveObraSerializer(serializers.Serializer):
    class Meta:
        model = Obra
        fields = '__all__'