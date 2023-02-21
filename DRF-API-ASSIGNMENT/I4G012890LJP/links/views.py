from rest_framework import generics
from .models import Link
from .serializers import Linkserializer


class PostListApi(generics.ListAPIView):
    queryset =Link.objects.filter(active=True)
    serializer_class = Linkserializer

class  PostCreateApi(generics.CreateAPIView):
    queryset =Link.objects.filter(active=True)
    serializer_class = Linkserializer    

class  PostDetailApi(generics.RetrieveAPIView):
    queryset =Link.objects.filter(active=True)
    serializer_class = Linkserializer

class  PostUpdateApi(generics.UpdateAPIView):
    queryset =Link.objects.filter(active=True)
    serializer_class = Linkserializer

class  PostDeleteApi(generics.DestroyAPIView):
    queryset =Link.objects.filter(active=True)
    serializer_class = Linkserializer    

