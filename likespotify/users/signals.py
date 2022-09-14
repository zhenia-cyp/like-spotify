from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from  playlists.models import Album

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
       Profile.objects.create(user=instance)

       try:
           dp = Album.objects.get(id=10)
           dp.user.add(instance)
           cure = Album.objects.get(id=7)
           cure.user.add(instance)
           stereophonics = Album.objects.get(id=5)
           stereophonics.user.add(instance)
           sadsvit = Album.objects.get(id=6)
           sadsvit.user.add(instance)
       except Exception as e:
                raise e
