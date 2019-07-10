from django.contrib import admin
from .models import Artist, Song, Playlist, Video
# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'image', 'language' )

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'url', 'language',  'genre')

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'cover_art')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'url', 'language', 'genre', 'image')



admin.site.register(Artist, ArtistAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Song, SongAdmin)