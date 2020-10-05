# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

LANGUAGE_CHOICES = (
    ("English", "English"),
    ("Nepali", "Nepali"),
    ("Hindi", "Hindi"),
    ("Dzongkha", "Dzongkha")
)

GENRE_CHOICES = (
    ("Unknown", "Unknown"),
    ("Movie", "Movie"),
    ("Pop", "Pop"),
    ("Rock", "Rock"),
    ("Alternative/Indie", "Alternative/Indie"),
    ("Remix", "Remix"),
    ("Instrumental", "Instrumental"),
    ("Folk", "Folk"),
    ("Electronic", "Electronic")
)
TYPE_STATUS = (
    (0, "ENABLE"),
    (1, "DISABLE")
)

ALIGNMENT_TYPES = (
    (0, "Left"),
    (1, "Center"),
    (2, "Right"),
)
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50)
    admin_email = models.TextField()
    admin_username = models.CharField(max_length=50)
    admin_password = models.TextField()
    status = models.CharField(
        choices=TYPE_STATUS,
        max_length=7
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'admin'


class AdsSettings(models.Model):
    ads_id = models.AutoField(primary_key=True)
    ads_title = models.TextField()
    ads_id_value = models.TextField()
    ads_status = models.CharField(max_length=7)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'ads_settings'


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    artist_id = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100, blank=True, null=True)
    album_image = models.CharField(max_length=100, blank=True, null=True)
    album_status = models.CharField(
        choices=TYPE_STATUS,
        max_length=7
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'album'


class ApiList(models.Model):
    api_id = models.AutoField(primary_key=True)
    api_name = models.TextField()
    api_link = models.TextField()
    api_type = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'api_list'


class ApiListParameters(models.Model):
    api_list_parameters_id = models.AutoField(primary_key=True)
    api_list_id = models.IntegerField()
    api_list_parameters_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'api_list_parameters'


class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=100, blank=True, null=True)
    artist_image = models.CharField(max_length=100, blank=True, null=True)
    artist_status = models.CharField(
        choices=TYPE_STATUS,
        max_length=7
    )
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'artist'


class BannerSlider(models.Model):
    banner_slider_id = models.AutoField(primary_key=True)
    banner_slider_name = models.CharField(max_length=1000, blank=True, null=True)
    banner_slider_name_alignment = models.CharField(max_length=6)
    banner_slider_image = models.CharField(max_length=1000)
    banner_slider_show_button = models.IntegerField()
    banner_slider_button_alignment = models.CharField(max_length=6)
    banner_slider_button_text = models.CharField(max_length=20, blank=True, null=True)
    banner_slider_order = models.IntegerField()
    banner_slider_status = models.CharField(
        choices=TYPE_STATUS,
        max_length=7
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'banner_slider'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    parent_category_id = models.IntegerField()
    category_status = models.CharField(
        choices=TYPE_STATUS,
        max_length=7
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'category'


class HomeComponents(models.Model):
    home_components_id = models.AutoField(primary_key=True)
    home_components_name = models.CharField(max_length=100)
    home_components_description = models.TextField()
    home_components_item_display_count = models.IntegerField(blank=True, null=True)
    home_components_order = models.IntegerField()
    home_components_status = models.CharField(
        choices=TYPE_STATUS,
        max_length=7
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'home_components'


class Liked(models.Model):
    like_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    like_type = models.CharField(max_length=7)
    like_type_id = models.IntegerField()
    like_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'liked'


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=500)
    movie_description = models.TextField()
    movie_image = models.CharField(max_length=100)
    movie_year = models.CharField(max_length=10)
    movie_status = models.CharField(
        choices=TYPE_STATUS,
        max_length=7
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'movie'


class Music(models.Model):
    music_id = models.AutoField(primary_key=True)
    music_title = models.TextField()
    music_file = models.CharField(max_length=100)
    music_image = models.CharField(max_length=100)
    category_id = models.IntegerField(blank=True, null=True)
    album_id = models.IntegerField()
    artist_id = models.CharField(max_length=100)
    movie_id = models.IntegerField(blank=True, null=True)
    music_size = models.CharField(max_length=50, blank=True, null=True)
    music_duration = models.CharField(max_length=10)
    music_status = models.CharField(
        choices=TYPE_STATUS,
        max_length=7
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'music'


class NotificationSettings(models.Model):
    notification_id = models.AutoField(primary_key=True)
    settings_name = models.TextField()
    settings_value = models.TextField()
    settings_status = models.CharField(max_length=7)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'notification_settings'


class PackageSettings(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=1000)
    package_duration = models.CharField(max_length=100)
    package_price = models.CharField(max_length=100)
    package_status = models.CharField(
        choices=TYPE_STATUS,
        max_length=7
    )
    package_note = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'package_settings'


class PaymentMethod(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    payment_method_name = models.CharField(max_length=100)
    payment_method_currency = models.CharField(max_length=10, blank=True, null=True)
    payment_method_public_key = models.CharField(max_length=255, blank=True, null=True)
    payment_method_secret_key = models.CharField(max_length=255, blank=True, null=True)
    payment_method_status = models.CharField(max_length=7)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'payment_method'


class RecentlyView(models.Model):
    recently_view_id = models.AutoField(primary_key=True)
    recently_view_type = models.CharField(max_length=6)
    recently_view_type_id = models.IntegerField()
    user_id = models.IntegerField()
    created_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'recently_view'


class SettingsFlag(models.Model):
    settings_flag_id = models.AutoField(primary_key=True)
    settings_flag_name = models.CharField(max_length=100)
    settings_flag_value = models.CharField(max_length=7)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'settings_flag'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField(blank=True, null=True)
    user_email = models.TextField(blank=True, null=True)
    user_password = models.TextField(blank=True, null=True)
    user_phone = models.CharField(max_length=30, blank=True, null=True)
    user_profile_pic = models.CharField(max_length=100, blank=True, null=True)
    user_package_id = models.IntegerField(blank=True, null=True)
    user_package_paid_date = models.DateTimeField(blank=True, null=True)
    user_package_expiry_date = models.DateTimeField(blank=True, null=True)
    user_token = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'user'


class UserPayment(models.Model):
    user_payment_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    package_id = models.IntegerField()
    card_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    card_number = models.IntegerField()
    cvc = models.IntegerField()
    expiration_month = models.IntegerField()
    expiration_year = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'user_payment'


class UserPlaylist(models.Model):
    user_playlist_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    user_playlist_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'user_playlist'


class UserPlaylistMusic(models.Model):
    user_playlist_music_id = models.AutoField(primary_key=True)
    user_playlist_id = models.IntegerField()
    user_id = models.IntegerField()
    music_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'user_playlist_music'
