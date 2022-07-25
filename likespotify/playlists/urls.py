
from django.urls import path
from playlists.views import PlaylistPageView, CreateNewAlbum,LoadSongUseAlbumViews
from playlists.views import SingerToSongViews,CurrentAlbumView


urlpatterns = [
    path("page/album/",PlaylistPageView.as_view(), name='create album'),
    path("create/new/album/",CreateNewAlbum.as_view()),
    path("current/album/<int:pk>",CurrentAlbumView.as_view()),
    path("album/song/<int:pk>",LoadSongUseAlbumViews.as_view(),name='load album song'),
    path("singer/",SingerToSongViews.as_view())
]
