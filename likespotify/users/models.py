from django.db import models
from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    """profile model"""
    user = models.OneToOneField(User, verbose_name='логин',on_delete=models.CASCADE)
    text = models.TextField('о себе', blank=True)
    photo = models.ImageField('photo', null=True, blank=True, upload_to='userpick')
    social_network = models.URLField('линк на соц сети', null=True, blank=True)

    def __str__(self):
        return '{0},{1},{2},{3} '.format(self.user,self.text,self.photo,self.social_network)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'



class ForEmailForm(models.Model):
    email = models.EmailField()