from django.db.models import fields
from rest_framework import serializers
from .models import Meme


class MyMemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = '__all__'


class CreatMemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = '__all__'

    def validate(self, attrs):

        return attrs

    def create(self, validate_data):
        return Meme.objects.create(**validate_data)
