from django.db.models import fields
from rest_framework import serializers
from .models import Meme


class MyMemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = '__all__'
