from django.contrib import admin
from .models import Artist, User, Music, Admin, UserPlaylist, UserPlaylistMusic,  Movie, Album, UserPayment, PaymentMethod,  NotificationSettings, PackageSettings, Category
from django.contrib.auth.admin import UserAdmin

class ArtistAdmin(admin.ModelAdmin):
    pass

class MusicAdmin(admin.ModelAdmin):
    pass

class UserPaymentAdmin(admin.ModelAdmin):
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


class MovieAdmin(admin.ModelAdmin):
    pass


class PackageSettingsAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class AdminAdmin(admin.ModelAdmin):
    pass

admin.site.register(Artist, ArtistAdmin)
admin.site.register(UserPlaylist, UserPlaylistAdmin)
admin.site.register(UserPlaylistMusic,UserPlaylistMusicAdmin )
admin.site.register(Movie, MovieAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(UserPayment, UserPaymentAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(NotificationSettings, NotificationSettingsAdmin)
admin.site.register(PackageSettings, PackageSettingsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Admin, AdminAdmin)