from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
User = get_user_model()
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

class Artist(models.Model):
    title = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000, blank=True)
    name = models.CharField(max_length=1000, blank=True)
    profileImageURL = models.CharField(max_length=2000, blank=True)
    thumbnailProfileImageURL = models.CharField(max_length=2000, blank=True)
    about = models.CharField(max_length=3000)
    stars = models.IntegerField(default=0)
    artist_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    language = models.CharField(max_length=10,
                                choices=LANGUAGE_CHOICES,
                                default=LANGUAGE_CHOICES[0][0])
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'artist'

    def __str__(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    title = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist, blank=True, on_delete=models.PROTECT)
    thumbnail = models.CharField(max_length=10000)
    stars = models.IntegerField(default=0)
    album_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    genre = models.CharField(max_length=50,
                             choices=GENRE_CHOICES,
                             default=GENRE_CHOICES[0][0])
    language = models.CharField(max_length=10,
                                choices=LANGUAGE_CHOICES,
                                default=LANGUAGE_CHOICES[0][0])
    duration = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'album'




class Video(models.Model):
    title = models.CharField(max_length=1000)
    lyrics = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist, blank=True, on_delete=models.PROTECT)
    url = models.CharField(max_length=1000)
    genre = models.CharField(max_length=50,
                             choices=GENRE_CHOICES,
                             default=GENRE_CHOICES[0][0])
    language = models.CharField(max_length=10,
                                choices=LANGUAGE_CHOICES,
                                default=LANGUAGE_CHOICES[0][0])
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist, blank=True, on_delete=models.PROTECT)
    fileName = models.CharField(max_length=1000)
    stars = models.IntegerField(default=0)
    imageURL = models.CharField(max_length=10000)
    thumbnailImageURL = models.CharField(max_length=10000)
    genre = models.CharField(max_length=50,
                             choices=GENRE_CHOICES,
                             default=GENRE_CHOICES[0][0])
    language = models.CharField(max_length=10,
                                choices=LANGUAGE_CHOICES,
                                default=LANGUAGE_CHOICES[0][0])

    album = models.ForeignKey(Album, blank=True, on_delete=models.PROTECT)
    duration = models.CharField(max_length=10000)
    durationInSeconds = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


    class Meta:
        db_table = 'music'

class UserPlaylist(models.Model):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT)
    cover_art = models.CharField(max_length=2000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'user_playlist'
    def __str__(self):
        return self.name

class UserPlaylistMusic(models.Model):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT)
    # called music on the the old api
    song = models.ForeignKey(Song, blank=True, on_delete=models.PROTECT)
    cover_art = models.CharField(max_length=2000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_playlist_music'



# UserPaymentMethod
class UserPaymentMethod(models.Model):
    user_payment_id = models.IntegerField()
    user_id = models.IntegerField()
    package_id = models.IntegerField()
    card_name = models.CharField(max_length=100)
    amount  = models.IntegerField()
    card_number = models.IntegerField(),
    cvc = models.IntegerField(),
    expiration_month = models.IntegerField(),
    expiration_year = models.IntegerField(),
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_payment'

# PaymentMethod options

class PaymentMethod(models.Model):
    payment_method_id = models.IntegerField()
    payment_method_name = models.CharField(max_length=100)
    payment_method_currency = models.CharField(max_length=10)
    payment_method_public_key = models.CharField(max_length=255)
    payment_method_secret_key = models.CharField(max_length=255)
    payment_method_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'payment_method'


# Notification Settings
class NotificationSettings(models.Model):
    notification_id = models.IntegerField()
    settings_name  = models.CharField(max_length=100)
    settings_value = models.CharField(max_length=100)
    settings_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    last_updated =  models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notification_settings'


#Package settings

class PackageSettings(models.Model):
    package_id = models.IntegerField()
    package_name = models.CharField(max_length=1000)
    package_duration = models.CharField(max_length=100)
    package_price = models.CharField(max_length=100)
    package_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    package_note = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'package_settings'

#categories/genres

class Category(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=100)
    parent_category_id = models.CharField(max_length=11)
    category_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'category'




# Settings Flag model
class SettingsFlag(models.Model):
    settings_flag_id = models.IntegerField()
    settings_flag_name = models.CharField(
        max_length=100,
    )
    settings_flag_valye = models.CharField(
        max_length=10,
        choices=TYPE_STATUS
    )
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'settings_flag'

# Home Compoonents
class HomeComponent(models.Model):
    home_components_id = models.IntegerField()
    home_components_name = models.CharField(max_length=100)
    home_components_description =  models.TextField()
    home_components_item_display_count = models.IntegerField()
    home_components_order = models.IntegerField()
    home_components_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'home_component'

# Banner Slider
class BannerSlider(models.Model):
    banner_slider_id = models.IntegerField()
    banner_slider_name = models.CharField(max_length=1000)
    banner_slider_name_alignment = models.CharField(
        max_length=10,
        choices=ALIGNMENT_TYPES
    )
    banner_slider_image = models.CharField(max_length=1000)
    banner_slider_show_button = models.IntegerField()
    banner_slider_button_alignment = models.CharField(
        choices=ALIGNMENT_TYPES,
        max_length=10
    )
    banner_slider_button_text = models.CharField(max_length=20)
    banner_slider_order = models.IntegerField()
    banner_slider_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS
    )
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'banner_slider'


