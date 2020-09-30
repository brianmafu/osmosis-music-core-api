from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
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

# General User on System
class User(AbstractUser):
    user_phone = models.CharField(max_length=30)
    user_profile_pic = models.CharField(max_length=100)
    user_package_id = models.IntegerField(default=0)
    user_package_paid_date = models.DateTimeField(auto_now=True)
    user_package_expiry_date = models.DateTimeField(auto_now=True)
    user_token = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    _user_id = models.IntegerField(default=-1)
    _user_name = models.CharField(max_length=300)
    _user_email = models.CharField(max_length=100)
    _user_password = models.CharField(max_length=100)
    @property
    def user_id(self):
       return self.id

    @property
    def user_name(self):
        return self.username

    @property
    def user_email(self):
        return self.email

    @property
    def user_password(self):
        return self.password

    # setters

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
        self.id = value

    @user_name.setter 
    def user_name(self, value):
        self._user_name = value
        self.username = value

    @user_email.setter
    def user_email(self, value):
        self._user_email = value
        self.email = value

    @user_password.setter
    def user_password(self, value):
        self.password = value
        self._user_password = value
    
    class Meta:
        db_table = 'user'

# Admin user
class Admin(User):
    
    # admin properties are base on the base user
    # marked as super user tho
    _admin_id = models.IntegerField(default=-1)
    _admin_name = models.CharField(
        max_length=200
    )
    _admin_email = models.CharField(
        max_length=200
    )
    _admin_username = models.CharField(
        max_length=30
    )

    _admin_password = models.CharField(
        max_length=100
    )
    # getters
    @property
    def admin_id(self):
        return self.super.user_id

    @property
    def admin_name(self):
        return self.super.user_name

    @property
    def admin_email(self):
        return self.super.user_email
    @property
    def admin_username(self):
        return self.super.user_name

    @property
    def admin_password(self):
        return self.user_password
    
    # setters
    @admin_id.setter
    def admin_id(self, value):
        self._admin_id = value
        self.super.user_id = value

    @admin_name.setter
    def admin_name(self, value):
        self._admin_username = value
        self.super.user_name = value

    @admin_email.setter
    def admin_email(self, value):
        self._admin_email = value
        self.super.user_email = value

    @admin_password.setter
    def admin_password(self, value):
        self._admin_password = value
        self.super.user_password = value

    status = models.CharField(
        max_length=100,
        choices=TYPE_STATUS
    )
    class Meta:
        db_table = 'admin'




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
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

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
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    # @property 
    # def artist_id(self):
    #     return self.artist.id

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
    created_date = models.DateTimeField(auto_now_add=True)

    # @property
    # def artist_id(self):
    #     return self.artist.id

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
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # @property
    # def artist_id(self):
    #     return self.artist.id

    # @property 
    # def album_id(self):
    #     return self.album.id

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'music'

class UserPlaylist(models.Model):
    name = models.CharField(max_length=1000)
    user =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    cover_art = models.CharField(max_length=2000, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    @property 
    def user_playlist_id(self):
        return self.id

    # @property
    # def user_id(self):
    #     return self.user.id

    class Meta:
        db_table = 'user_playlist'
    def __str__(self):
        return self.name

class UserPlaylistMusic(models.Model):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    # called music on the the old api
    song = models.ForeignKey(Song, blank=True, on_delete=models.PROTECT)
    cover_art = models.CharField(max_length=2000, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    @property 
    def user_playlist_music_id(self):
        return self.id

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_playlist_music'



# UserPaymentMethod
class UserPaymentMethod(models.Model):
    # user_payment_id = models.IntegerField()
    user_id = models.IntegerField()
    package_id = models.IntegerField()
    card_name = models.CharField(max_length=100)
    amount  = models.IntegerField()
    card_number = models.IntegerField(),
    cvc = models.IntegerField(),
    expiration_month = models.IntegerField(),
    expiration_year = models.IntegerField(),
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def user_payment_id(self):
        return self.id

    class Meta:
        db_table = 'user_payment'

# PaymentMethod options

class PaymentMethod(models.Model):
    # payment_method_id = models.IntegerField()
    payment_method_name = models.CharField(max_length=100)
    payment_method_currency = models.CharField(max_length=10)
    payment_method_public_key = models.CharField(max_length=255)
    payment_method_secret_key = models.CharField(max_length=255)
    payment_method_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def payment_method_id(self):
        return self.id

    class Meta:
        db_table = 'payment_method'


# Notification Settings
class NotificationSettings(models.Model):
    # notification_id = models.IntegerField()
    settings_name  = models.CharField(max_length=100)
    settings_value = models.CharField(max_length=100)
    settings_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    last_updated =  models.DateTimeField(auto_now=True)

    @property
    def notification_id(self):
        return self.id
    class Meta:
        db_table = 'notification_settings'


#Package settings

class PackageSettings(models.Model):
    # package_id = models.IntegerField()
    package_name = models.CharField(max_length=1000)
    package_duration = models.CharField(max_length=100)
    package_price = models.CharField(max_length=100)
    package_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    package_note = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def package_id(self):
        return self.id

    class Meta:
        db_table = 'package_settings'

#categories/genres

class Category(models.Model):
    # category_id = models.IntegerField()
    category_name = models.CharField(max_length=100)
    parent_category_id = models.CharField(max_length=11)
    category_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    created_date = models.DateTimeField(auto_now_add=True)
    @property
    def category_id(self):
        return self.id
    class Meta:
        db_table = 'category'




# Settings Flag model
class SettingsFlag(models.Model):
    # settings_flag_id = models.IntegerField()
    settings_flag_name = models.CharField(
        max_length=100,
    )
    settings_flag_valye = models.CharField(
        max_length=10,
        choices=TYPE_STATUS
    )
    created_date = models.DateTimeField(auto_now_add=True)
    @property
    def settings_flag_id(self):
        return self.id
    class Meta:
        db_table = 'settings_flag'

# Home Compoonents
class HomeComponent(models.Model):
    # home_components_id = models.IntegerField()
    home_components_name = models.CharField(max_length=100)
    home_components_description =  models.TextField()
    home_components_item_display_count = models.IntegerField()
    home_components_order = models.IntegerField()
    home_components_status = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)
    created_date = models.DateTimeField(auto_now_add=True)
    @property
    def home_components_id(self):
        return self.id
    class Meta:
        db_table = 'home_component'

# Banner Slider
class BannerSlider(models.Model):
    # banner_slider_id = models.IntegerField()
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
    @property
    def banner_slider_id(self):
        return self.id
    class Meta:
        db_table = 'banner_slider'


