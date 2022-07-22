import datetime
from django.views.generic.base import TemplateView, View
from playlists.forms import AlbumForm
from django.contrib import messages
from django.shortcuts import redirect

from playlists.models import Album


class PlaylistPageView(TemplateView):
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
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            messages.success(request, 'альбом создан!')
            return redirect('profile')
        else:
            print(album_form.errors)
            messages.error(request, 'Ошибка! Попробуйте еще раз')
            return redirect('create album')