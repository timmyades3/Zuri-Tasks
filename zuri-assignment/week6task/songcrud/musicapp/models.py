from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Artiste(models.Model):
  first_name = models.CharField(max_length=50, null=True)
  last_name = models.CharField(max_length=50, null=True)
  age = models.IntegerField(null=True)


  def __str__(self):
    return self.first_name+' '+self.last_name


class Song(models.Model):
  artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=100, null=True)
  date_released = models.DateTimeField(default=timezone.now, null=True)
  likes = models.ManyToManyField(User, related_name='liked_songs')


  def __str__(self):
    return self.title


class Lyrics(models.Model):
  song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
  content = models.TextField(null=True)


  def __str__(self):
    return self.song.title