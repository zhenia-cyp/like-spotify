from django.contrib import admin

from playlists.models import Song, Album


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','singer','get_album','song','image')

admin.site.register(Song,SongAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

admin.site.register(Album,AlbumAdmin)