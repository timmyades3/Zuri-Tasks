from django.urls import path
from . import views


urlpatterns = [
    path('',views.Apioverview.as_view(),name='api-overview'),
    path('artiste_list/',views.Artistelist.as_view(),name='artiste-list'),
    path('artiste_create/',views.Artistecreate.as_view(),name='artiste-create'),
    path('artiste_detail/<int:pk>/',views.Artistedetail.as_view(),name='artiste-detail'),
    path('artiste_update/<int:pk>/',views.Artisteupdate.as_view(),name='artiste-update'),
    path('artiste_delete/<int:pk>/',views.Artistedelete.as_view(),name='artiste-delete'),
    path('song_list/',views.Songlist.as_view(),name='song-list'),
    path('song_create/',views.Songcreate.as_view(),name='song-create'),
    path('song_detail/<int:pk>/',views.Songdetail.as_view(),name='song-detail'),
    path('song_update/<int:pk>/',views.Songupdate.as_view(),name='song-update'),
    path('song_delete/<int:pk>/',views.Songdelete.as_view(),name='song-delete'),
]