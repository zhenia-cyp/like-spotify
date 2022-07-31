
from django.urls import path
from playlists.views import CreateNewAlbum,LoadSongUseAlbumViews
from playlists.views import SingerToSongViews,CurrentAlbumView,SearchPageView,AlbumPageView


urlpatterns = [
    path("page/album/",AlbumPageView.as_view(), name='create album'),
    path("create/new/album/",CreateNewAlbum.as_view()),
    path("current/album/<int:pk>",CurrentAlbumView.as_view()),
    path("album/song/<int:pk>",LoadSongUseAlbumViews.as_view(),name='load album song'),
    path("singer/",SingerToSongViews.as_view()),
    path("search/", SearchPageView.as_view(), name='search page'),
]
