from django.db import models
from django.contrib.auth.models import User


class Domain(models.Model):
    """domian name"""
    name = models.CharField('домен', max_length=250)

    def __str__(self):
        return '{0} '.format(self.name)

    class Meta:
        verbose_name = 'Доменное имя'
        verbose_name_plural = 'Доменные имена'



class ShortLink(models.Model):
    """short url"""
    domen = models.ForeignKey(Domain, verbose_name='домен',on_delete=models.CASCADE)
    long_url = models.CharField('длинная ссылка',max_length=200)
    short_url = models.CharField('сокращенная ссылка',max_length=200,unique=True)
    clicks = models.IntegerField('количество кликов',default=0, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    lifetime = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return '{0}'.format(self.short_url)

    def get_short_link(self):
        return self.domen.name + self.short_url

    class Meta:
        verbose_name = 'Короткая ссылка'
        verbose_name_plural = 'Короткая ссылки'