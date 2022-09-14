from django import forms
from playlists.models import Song,Album,Singer,Category



class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'



class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields = '__all__'



class SingerForm(forms.ModelForm):
    class Meta:
        model=Singer
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields = '__all__'
