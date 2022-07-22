
from django.urls import path

from playlists.views import PlaylistPageView, CreateNewAlbum

urlpatterns = [
    path("page/album/",PlaylistPageView.as_view(), name='create album'),
    path("create/new/album/",CreateNewAlbum.as_view()),
]
