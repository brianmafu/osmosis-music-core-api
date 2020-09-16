from django.contrib import admin
from .models import Artist, Song, UserPlaylist, UserPlaylistMusic,  Video, Album, UserPaymentMethod, PaymentMethod,  NotificationSettings, PackageSettings
# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    pass

class SongAdmin(admin.ModelAdmin):
    pass

class UserPaymentMethodAdmin(admin.ModelAdmin):
    pass

class PaymentMethodAdmin(admin.ModelAdmin):
    pass

class AlbumAdmin(admin.ModelAdmin):
    pass

class UserPlaylistAdmin(admin.ModelAdmin):
    pass

class UserPlaylistMusicAdmin(admin.ModelAdmin):
    pass

class NotificationSettingsAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


class PackageSettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artist, ArtistAdmin)
admin.site.register(UserPlaylist, UserPlaylistAdmin)
admin.site.regster(UserPlaylistMusic,UserPlaylistMusicAdmin )
admin.site.register(Video, VideoAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(UserPaymentMethod, UserPaymentMethodAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(NotificationSettings, NotificationSettingsAdmin)
admin.site.register(PackageSettings, PackageSettingsAdmin)