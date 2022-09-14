from django.db import models
from django.contrib.auth.models import User


class Singer(models.Model):
    """singer"""
    name = models.CharField('имя исполнителя', max_length=150)

    def __str__(self):
        return '{0} '.format(self.name)

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Category(models.Model):
    """category"""
    name = models.CharField('категория', max_length=150)

    def __str__(self):
        return '{0} '.format(self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Album(models.Model):
    """album"""
    name = models.CharField('название', max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
    type = models.CharField('тип', max_length=150,default='альбом')
    image = models.ImageField(upload_to='playlist_images/',null=True, blank=True)
    quantity = models.CharField('количество треков',max_length=150,null=True, blank=True)
    year = models.CharField('год создания',max_length=150, null=True, blank=True,)
    user = models.ManyToManyField(User,verbose_name='альбом юзера',blank=True)
    singer = models.ManyToManyField(Singer,verbose_name='исполнитель')
    creator = models.ForeignKey(User,related_name ='acreator',on_delete=models.CASCADE)


    def __str__(self):
        return '{0} {1} {2} {3}' .format(self.id,self.name,self.category,self.singer,self.year,self.creator)

    def get_creator(self):
        return self.creator

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'




class Playlist(models.Model):
    """playlist"""
    name = models.CharField('название', max_length=150)
    type = models.CharField('тип',max_length=150,default='плейлист')
    user = models.ManyToManyField(User,verbose_name='юзер',blank=True)
    creator = models.ForeignKey(User,related_name='pcreator',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='playlist_images/')

    def __str__(self):
        return '{0} ' .format(self.name)

    class Meta:
        verbose_name = 'Плейлист'
        verbose_name_plural = 'Плейлисты'




class Song(models.Model):
    """song"""
    song = models.FileField(upload_to='songs')
    image = models.ImageField(upload_to='songs_images',blank=True)
    name = models.CharField('название',max_length=150)
    singer = models.ForeignKey(Singer,verbose_name='исполнитель',on_delete=models.CASCADE,null=True,blank=True)
    album = models.ManyToManyField(Album,verbose_name='альбом',null=True,blank=True)
    playlist = models.ManyToManyField(Playlist,verbose_name='плейлист',null=True, blank=True)
    text= models.TextField(verbose_name='текст песни',null=True, blank=True)

    def __str__(self):
        return '{0} {1} {2}' .format(self.name,self.song,self.singer)

    def get_album(self):
        return ",".join([str(p) for p in self.album.all()])

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'