from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artiste,Song
from .serializers import Artisteserializer,Songserializer, Songupdateserializer

# Create your views here.


class Apioverview(APIView):
  def get(self, request):

    api_urls = {
  'List.': '/artiste_list/',
  'Detail.': '/artiste_detail/<str:pk>/', 
  'Create.': '/artiste_create/',
  'Update.': '/artiste_update/<str:pk>/',
  'Delete.': '/artiste_delete/<str:pk>/',
  'List': '/song_list/',
  'Detail': '/song_detail/<str:pk>/', 
  'Create': '/song_create/',
  'Update': '/song_update/<str:pk>/',
  'Delete': '/song_delete/<str:pk>/',
  }

    return Response(api_urls)


#Artiste api class based views
class Artistelist(generics.ListAPIView):
  queryset = Artiste.objects.all()
  serializer_class = Artisteserializer


class Artistecreate(generics.CreateAPIView):
  queryset = Artiste.objects.all()
  serializer_class = Artisteserializer


class Artisteupdate(generics.UpdateAPIView):
  queryset = Artiste.objects.all()
  serializer_class = Artisteserializer


class Artistedetail(generics.RetrieveAPIView):
  queryset = Artiste.objects.all()
  serializer_class = Artisteserializer


class Artistedelete(generics.DestroyAPIView):
  queryset = Artiste.objects.all()
  serializer_class = Artisteserializer


#Song api class based views
class Songlist(generics.ListAPIView):
  queryset = Song.objects.all()
  serializer_class = Songserializer


class Songcreate(generics.CreateAPIView):
  queryset = Song.objects.all()
  serializer_class = Songserializer


class Songupdate(generics.UpdateAPIView):
  queryset = Song.objects.all()
  serializer_class = Songupdateserializer


class Songdetail(generics.RetrieveAPIView):
  queryset = Song.objects.all()
  serializer_class = Songserializer


class Songdelete(generics.DestroyAPIView):
  queryset = Song.objects.all()
  serializer_class = Songserializer


