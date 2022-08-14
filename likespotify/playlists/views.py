import datetime
from django.views.generic import DetailView
from django.views.generic.base import TemplateView, View
from playlists.forms import  SongForm,AlbumForm
from django.contrib import messages
from django.shortcuts import redirect, render
from playlists.models import Album,Song
from playlists.forms import SingerForm,SongForm
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView



class HomePage(TemplateView):
    template_name = 'playlist/home.html'



class TakeAlbumView(View):
    """take another user's album"""
    def get_object(self,request,*args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            return Album.objects.get(id=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self,request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        album = self.get_object(pk)
        album.user.add(request.user)
        return redirect('profile')



class DeleteAlbumView(DetailView):
    """delete album by id"""
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            return Album.objects.get(id=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = self.get_object(pk)
        obj.delete()
        return redirect('profile')



class SearchPageView(View):
    """search system"""
    def get(self, request):
        template = 'playlist/search_page.html'
        all_albums = Album.objects.all()
        own_albums = Album.objects.filter(creator=request.user)
        own_albums_ids = get_id_ownalbums(own_albums)
        added_albums = Album.objects.filter(user=request.user)
        print('added_albums:',added_albums)
        return render(request, template, {'all_albums': all_albums,'own_albums_ids':own_albums_ids,'added_albums':added_albums})


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
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            return Album.objects.get(id=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        current_album = self.get_object(pk)
        albumform = AlbumForm(instance=current_album)
        return render(self.request,'playlist/edit_album.html',{'albumform': albumform,'current_album':current_album})

    def post(self,request,*args, **kwargs):
        pk = self.kwargs.get('pk')
        album = get_object_or_404(Album,id=pk)
        albumform = AlbumForm(request.POST,request.FILES)
        if albumform.is_valid():
            albumform.save(commit=False)
            creator = get_object_or_404(User, id=request.POST['creator'])
            album.id=pk
            album.name=request.POST['name']
            album.image = request.FILES['image']
            album.type=request.POST['type']
            album.year=request.POST['year']
            album.singer.add(request.POST['singer'])
            album.user.add(request.POST['user'])
            album.creator = creator
            album.save()
            return redirect('profile')
        else:
            print(albumform.errors)
            return redirect('create album')



class CurrentAlbumView(DetailView):
    """class to get current album"""
    model = Album
    template_name = 'playlist/album_detail.html'

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        current_album = Album.objects.get(id=self.kwargs.get('pk'))
        query_set = current_album.song_set.all()
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
            singer_form.save()
            return redirect('create album')
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
        if song_form.is_valid():
            song_form.save()
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
            return redirect('profile')
        else:
            print(album_form.errors)
            messages.error(request, 'Ошибка! Попробуйте еще раз')
            return redirect('create album')


class BreakAddedAlbum(DetailView):
    """this class removes a user from the added album"""
    def get(self,request, *args, **kwargs):
        album = get_object_or_404(Album, id=self.kwargs.get('pk'))
        album.user.remove(self.request.user)
        return redirect('profile')



def get_id_ownalbums(own_albums):
    """function return albums ids"""
    own_id = []
    for album in own_albums:
        own_id.append(album.id)
    return own_id



