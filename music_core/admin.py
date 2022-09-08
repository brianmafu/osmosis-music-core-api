from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Admin,
    Album,
    Artist,
    Category,
    Movie,
    Music,
    NotificationSettings,
    PackageSettings,
    PaymentMethod,
    User,
    UserPayment,
    UserPlaylist,
    UserPlaylistMusic,
)


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


class MyUserAdmin(UserAdmin):
    model = User
    list_display = ()  # Contain only fields in your `custom-user-model`
    list_filter = ()  # Contain only fields in your `custom-user-model` intended for filtering. Do not include `groups`since you do not have it
    search_fields = ()  # Contain only fields in your `custom-user-model` intended for searching
    ordering = ()  # Contain only fields in your `custom-user-model` intended to ordering
    filter_horizontal = ()  # Leave it empty. You have neither `groups` or `user_permissions`
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("__all__",)}),)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(UserPlaylist, UserPlaylistAdmin)
admin.site.register(UserPlaylistMusic, UserPlaylistMusicAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(UserPayment, UserPaymentAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(NotificationSettings, NotificationSettingsAdmin)
admin.site.register(PackageSettings, PackageSettingsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, MyUserAdmin)
admin.site.register(Admin, AdminAdmin)
