from django.contrib import admin
from .models import Artist, Song, Playlist, Video, Album
# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name', 'name', 'language', 'profileImageURL', 'thumbnailProfileImageURL', 'about' , 'stars')

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist',  'language', 'album', 'description',  'genre', 'imageURL',  'thumbnailImageURL',  'fileName', 'stars', 'duration', 'durationInSeconds')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'thumbnail', 'language',  'genre', 'stars', 'duration')

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'cover_art')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'url', 'language', 'genre', 'image')



admin.site.register(Artist, ArtistAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
