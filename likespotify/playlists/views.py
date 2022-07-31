import datetime

from django.views.generic import DetailView
from django.views.generic.base import TemplateView, View
from playlists.forms import  SongForm,AlbumForm
from django.contrib import messages
from django.shortcuts import redirect, render
from playlists.models import Album,Song
from playlists.forms import SingerForm,SongForm



class SearchPageView(View):
    """search system"""
    def get(self, request):
        template = 'playlist/search_page.html'
        return render(request, template, {})

    def post(self, request):
        template = 'playlist/search_page.html'
        search_query = self.request.POST.get('search', '')
        print('post search_query',search_query)
        if search_query:
            all_albums = Album.objects.filter(name__icontains=search_query)
            songs = Song.objects.filter(name__icontains=search_query)
            return render(request, template, {'all_albums': all_albums,'songs':songs})

        return render(request, template, {})



class EditAlbumView(View):
    """edit album"""
    def post(self,request):
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()

            return redirect('profile')
        else:
            print(album_form.errors)
            messages.error(request, 'Ошибка! Попробуйте еще раз')
            return redirect('create album')



class CurrentAlbumView(DetailView):
    """class to get current album"""
    model = Album
    template_name = 'playlist/album_detail.html'

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        current_album = Album.objects.get(id=self.kwargs.get('pk'))
        query_set = current_album.song_set.all()
        print('songs ', query_set)
        print('current_album  ', current_album)
        print('current_album  ', current_album.image)
        context['query_set'] = query_set
        return context


class SingerToSongViews(View):
    """the class leads to the page for creating a new song use album"""
    def get(self,request):
        template = 'playlist/singer.html'
        singer_form = SingerForm()
        return render(request,template,{'singerform':singer_form})

    def post(self, request,):
        singer_form = SingerForm(request.POST)
        if singer_form.is_valid():
            print('singerform')
            singer_form.save()
            return redirect('/playlist/album/song/')
        else:
            print(singer_form.errors)
            return redirect('create album')


class LoadSongUseAlbumViews(View):
    """the class leads to the page for creating a new song use album"""
    def get(self,request,pk):
        template = 'playlist/album_song.html'
        current_album = Album.objects.get(id=pk)
        song_form = SongForm(initial={'user': self.request.user,'album':current_album})
        return render(request,template,{'songform':song_form,'num':current_album.id})

    def post(self, request,pk):
        song_form = SongForm(request.POST,request.FILES)
        print('post:::',request.POST)
        if song_form.is_valid():
            song_form.save()
            print('*', )
            return redirect('profile')
        else:
            print('**',song_form.errors)
            return redirect('create album')



class AlbumPageView(TemplateView):
    """this class leads to the create_album.html page """
    template_name = 'playlist/create_album.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album_form = AlbumForm(initial={'user': self.request.user,'year':datetime.date.today().year,'creator':self.request.user})
        context['albumform'] = album_form
        albums = Album.objects.filter(user=self.request.user)
        context['albums']=albums
        return context



class CreateNewAlbum(View):
    """create new album"""
    def post(self,request):
        album_form = AlbumForm(request.POST,request.FILES)
        if album_form.is_valid():
            album_form.save()
            print('_____', request.FILES)
            return redirect('profile')
        else:
            print(album_form.errors)
            messages.error(request, 'Ошибка! Попробуйте еще раз')
            return redirect('create album')


