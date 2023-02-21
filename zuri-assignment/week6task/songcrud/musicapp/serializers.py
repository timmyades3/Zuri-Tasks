from rest_framework import serializers
from .models import Artiste, Song


class Artisteserializer(serializers.ModelSerializer):
  class Meta:
    model = Artiste
    fields = '__all__'


class Songserializer(serializers.ModelSerializer):
  class Meta:
    model = Song
    fields = '__all__'


class Songupdateserializer(serializers.ModelSerializer):
  class Meta:
    model = Song
    fields = ['title','date_released']
