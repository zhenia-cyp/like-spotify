
from django.urls import path
from playlists.views import CreateNewAlbum,LoadSongUseAlbumViews,DeleteAlbumView,TakeAlbumView
from playlists.views import SingerToSongViews,CurrentAlbumView,SearchPageView,AlbumPageView,EditAlbumView
from playlists.views import HomePageView,BreakAddedAlbum,CategoryPage,SongDeleteView


urlpatterns = [
    path("page/album/",AlbumPageView.as_view(), name='create album'),
    path("create/new/album/",CreateNewAlbum.as_view(),),
    path("current/album/<int:pk>/",CurrentAlbumView.as_view(),name='list songs'),
    path("album/song/<int:pk>",LoadSongUseAlbumViews.as_view(),name='load album song'),
    path("singer/",SingerToSongViews.as_view()),
    path("delete/current/album/<int:pk>/",DeleteAlbumView.as_view()),
    path("search/", SearchPageView.as_view(), name='search page'),
    path("take/album/<int:pk>/",TakeAlbumView.as_view()),
    path("edit/album/<int:pk>/",EditAlbumView.as_view()),
    path("home/",HomePageView.as_view(), name='home'),
    path("category/",CategoryPage.as_view(), name='category'),
    path("break/added/album/<int:pk>/",BreakAddedAlbum.as_view(),),
    path("delete/song/<int:pk>/",SongDeleteView.as_view(),name='delete song'),

]
