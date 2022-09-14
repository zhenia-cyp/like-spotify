# Generated by Django 4.0.6 on 2022-08-23 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('type', models.CharField(default='альбом', max_length=150, verbose_name='тип')),
                ('image', models.ImageField(blank=True, null=True, upload_to='playlist_images/')),
                ('quantity', models.CharField(blank=True, max_length=150, null=True, verbose_name='количество треков')),
                ('year', models.CharField(blank=True, max_length=150, null=True, verbose_name='год создания')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('type', models.CharField(default='плейлист', max_length=150, verbose_name='тип')),
                ('image', models.ImageField(upload_to='playlist_images/')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pcreator', to=settings.AUTH_USER_MODEL)),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='юзер')),
            ],
            options={
                'verbose_name': 'Плейлист',
                'verbose_name_plural': 'Плейлисты',
            },
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='имя исполнителя')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.FileField(upload_to='songs')),
                ('image', models.ImageField(blank=True, upload_to='songs_images')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('text', models.TextField(blank=True, null=True, verbose_name='текст песни')),
                ('album', models.ManyToManyField(blank=True, null=True, to='playlists.album', verbose_name='альбом')),
                ('playlist', models.ManyToManyField(blank=True, null=True, to='playlists.playlist', verbose_name='плейлист')),
                ('singer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playlists.singer', verbose_name='исполнитель')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playlists.category'),
        ),
        migrations.AddField(
            model_name='album',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acreator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='singer',
            field=models.ManyToManyField(to='playlists.singer', verbose_name='исполнитель'),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='альбом юзера'),
        ),
    ]
