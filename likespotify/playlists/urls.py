
from django.urls import path
from playlists.views import CreateNewAlbum,LoadSongUseAlbumViews,DeleteAlbumView,TakeAlbumView
from playlists.views import SingerToSongViews,CurrentAlbumView,SearchPageView,AlbumPageView,EditAlbumView
from playlists.views import HomePage,BreakAddedAlbum


urlpatterns = [
    path("page/album/",AlbumPageView.as_view(), name='create album'),
    path("create/new/album/",CreateNewAlbum.as_view()),
    path("current/album/<int:pk>",CurrentAlbumView.as_view()),
    path("album/song/<int:pk>",LoadSongUseAlbumViews.as_view(),name='load album song'),
    path("singer/",SingerToSongViews.as_view()),
    path("delete/current/album/<int:pk>/",DeleteAlbumView.as_view()),
    path("search/", SearchPageView.as_view(), name='search page'),
    path("take/album/<int:pk>/",TakeAlbumView.as_view()),
    path("edit/album/<int:pk>/",EditAlbumView.as_view()),
    path("home/",HomePage.as_view(), name='home'),
    path("break/added/album/<int:pk>/",BreakAddedAlbum.as_view(),)
]
