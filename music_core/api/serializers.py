from rest_framework import serializers
from music_core.models import Artist, UserPlaylist, UserPlaylistMusic, \
    Song, Video, Album, \
    UserPaymentMethod, PaymentMethod, \
    NotificationSettings, PackageSettings

# Playlist Serializer
class  UserPlaylistSerializer(serializers.ModelSerializer):
    user_playlist_id = serializers.IntegerField(source='pk')
    user_id = serializers.IntegerField(source='user.id')
    user_playlist_name = serializers.CharField(source='name')
    class Meta:
        model = UserPlaylist
        fields = [
            'pk',
            'name',
            'cover_art',
            'user', 
            'user_playlist_id',
            'user_playlist_name'
        ]
  
    def create(self, data):
        name = data['name']
        cover_art = data['cover_art']

        play_list = UserPlaylist(
            name=name,
            cover_art=cover_art,
        )
        play_list.save()
        data['id'] =  play_list.id
        return data

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.cover_art = data.get('cover_art', instance.cover_art)
        instance.save()


# User Playlist to song assoication
class  UserPlaylistMusicSerializer(serializers.ModelSerializer):
    user_playlist_music_id = serializers.IntegerField(source='pk')
    user_id = serializers.IntegerField(source='user.id')
    user_playlist_music_name = serializers.CharField(source='name')
    class Meta:
        model = UserPlaylistMusic
        fields = [
            'pk',
            'name',
            'user_playlist_music_id',
            'user_id',
            'user_playlist_music_name',
            'cover_art',
            'user', 
            'song',
        ]
  
    def create(self, data):
        name = data['name']
        cover_art = data['cover_art']

        play_list = UserPlaylistMusic(
            name=name,
            cover_art=cover_art,
        )
        play_list.save()
        data['id'] =  play_list.id
        return data

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.cover_art = data.get('cover_art', instance.cover_art)
        instance.save()


# Artist Serializer
class  ArtistSerializer(serializers.ModelSerializer):
    artist_id = serializers.IntegerField(source='pk')
    artist_name = serializers.CharField(source='title')
    artist_image = serializers.CharField(source='profileImageURL')
    class Meta:
        model = Artist
        fields = [
            'pk',
            'title',
            'first_name',
            'last_name',
            'name', 
            'language',
            'profileImageURL',
            'artist_name',
            'artist_image',
            'artist_id',
            'artist_status',
            'thumbnailProfileImageURL',
            'about',
            'stars'           

        ]
  
    def create(self, data):
        title = data.get('title', None)
        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)
        language = data.get('language', None)
        name = data.get('name', None)
        profileImageURL = data.get('profileImageURL',None)
        thumbnailProfileImageURL = data.get('thumbnailProfileImageURL',
        None)
        about = data.get('about', None)
        stars = data.get('stars', None)

        artist = Artist(
            title=title,
            first_name=first_name,
            last_name=last_name,
            language=language,
            name=name,
            profileImageURL = profileImageURL,
            thumbnailProfileImageURL = thumbnailProfileImageURL,
            about=about,
            stars=stars
        )
        artist.save()
        data['id'] =  artist.id
        return data

    def update(self, instance, data):
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.language = data.get('language', instance.language)
        instance.title = data.get('title', instance.title)
        instance.name = data.get('name', instance.name)
        instance.profileImageURL = data.get('profileImageURL', instance.profileImageURL)
        instance.thumbnailProfileImageURL = data.get('thumbnailProfileImageURL', instance.thumbnailProfileImageURL)
        instance.stars = data.get('stars', instance.stars)
        instance.about = data.get('about', instance.about)
        instance.save()


# Album Serializer
class  AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=False, read_only=True)
    album_id = serializers.IntegerField(source='pk')
    artist_id = serializers.IntegerField(source='artist.pk')
    album_name = serializers.CharField(source='title')
    album_image = serializers.CharField(source='thumbnail')
    class Meta:
        model = Album
        fields = [
            'pk',
            'title',
            'artist',
            'thumbnail',
            'genre',
            'language',
            'stars',
            'duration',
            'album_id',
            'artist_id',
            'album_name',
            'album_image',
            'album_status',
        ]
  
    def create(self, data):
        title = data.get('title', None)
        artist_id = data.get('artist_id', None)
        genre = data.get('genre', "Unknown")
        language=data.get('language', None)
        stars = data.get('stars', 0)
        thumbnail = data.get('thumbnail', None) 
        duration = data.get('duration', 0)
        artists = Artist.objects.filter(id=int(artist_id))
        artist = None
        if artists:
            artist = artists[0]
        album = Album(
            title=title,
            artist=artist,
            genre=genre,
            thumbnail=thumbnail,
            language=language,
            duration=duration,
            stars=stars

        )
        album.save()
        data['id'] =  album.id
        return data

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.genre = data.get('genre', instance.genre)
        instance.stars = data.get('stars', instance.stars)
        instance.language = data.get('language', instance.language)
        instance.genre = data.get('genre', instance.genre)
        instance.duration = data.get('duration', instance.duration)
        artist = Artist.objects.filter(id=int(data.get('artist_id', 1)))
        artist = artist[0] if artist else None
        album = Album.objects.filter(id=int(data.get('album_id', 1)))
        album = album[0] if album else None
        thumbnail = data.get('thumbnail', instance.language)
        instance.artist = artist or None
        instance.album = album or None
        instance.save()


# Song Serializer
class  SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=False, read_only=True)
    album = AlbumSerializer(many=False, read_only=True)
    class Meta:
        model = Song
        fields = [
            'pk',
            'title',
            'artist',
            'stars',
            'fileName',
            'duration',
            'durationInSeconds',
            'imageURL',
            'thumbnailImageURL',
            'description',
            'album',
            'genre',
            'language',
        ]
  
    def create(self, data):
        title = data.get('title', None)
        artist_id=data.get('artist_id', 1)
        genre = data.get('genre', "Unknown")
        print("Genre: {0}".format(genre))
        stars = data.get('stars', 0)
        language = data.get('language', None) 
        imageURL = data.get('imageURL', None)
        fileName = data.get('fileName', None)
        thumbnailImageURL = data.get('thumbnailImageURL', None)
        album_id=data.get('album_id', 1)
        album=Album.objects.filter(id=int(album_id))
        album = album[0] if album else None  
        duration = data.get('duration', 0)
        description = data.get('description', None)
        durationInSeconds = data.get('durationInSeconds', 0 )
        artist = Artist.objects.filter(id=int(artist_id))
        artist = artist[0] if artist else None  

        song = Song(
            title = title or None,
            artist = artist or None,
            genre = genre or "Unknown",
            imageURL = imageURL or None,
            thumbnailImageURL = thumbnailImageURL or None,
            album = album or None,
            language = language or None,
            stars = stars or None,
            duration = duration or None,
            description = description or None,
            durationInSeconds = durationInSeconds or None,
            fileName = fileName or None
        )
        song.save()
        data['id'] =  song.id
        return data

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.fileName = data.get('fileName', instance.fileName)
        instance.language = data.get('language', instance.language)
        instance.duration = data.get('duration', instance.duration)
        instance.durationInSeconds = data.get('durationInSeconds', instance.durationInSeconds)
        instance.imageURL = data.get('imageURL', instance.ImageURL)
        instance.thumbnailImageURL = data.get('thubnailImageURL', instance.thumbnailImageURL)
        instance.stars = data.get('stars', instance.stars)
        instance.genre = data.get('genre', instance.genre)
        artist = Artist.objects.filter(id=int(data.get('artist_id', 1)))
        artist = artist[0] if artist else None
        album = Album.objects.filter(id=int(data.get('album_id', 1)))
        album = album[0] if album else None
        instance.artist = artist or None
        instance.album = album or None
        instance.save()


# Video Serializer
class  VideoSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=False, read_only=True)
    class Meta:
        model = Video
        fields = [
            'pk', 
            'title',
            'url',
            'artist',
            'genre',
            'language',
            'image',
        ]
  
    def create(self, data):
        title = data.get('title', None)
        url = data.get('url', None)
        genre = data.get('genre', None)
        artist_id = data.get('artist_id', -1)
        artists = Artist.objects.filter(id=int(artist_id))
        artist = None
        if artists:
            artist = artists[0]
        language = data.get('language', None)
        thumbnail = data.get('thumbnail', None)

        video = Video(
            title=title,
            url=url,
            artist=artist or None,
            language=language,
            image=thumbnail,
        )
        video.save()
        data['id'] =  video.id
        return data

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.url = data.get('url', instance.url)
        artist = Artist.objects.filter(id=int(data.get('artist_id', -1)))[:1]
        instance.artist = artist or None
        instance.language = data.get('language', instance.language)
        instance.image = data.get('image', instance.image)
        instance.save()

# UserPayment method serializer
class UserPaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPaymentMethod
        fields = ['__all__']

    def  create(self, data):
        user_id = data.get('user_id', None)
        package_id = data.get('package_id' , None)
        card_name = data.get('card_name',  None)
        amount = data.get('amount',  None)
        card_number = data.get('card_number',  None)
        cvc = data.get('cvc', None)
        expiration_month = data.get('expiration_month', None)
        expiration_year = data.get('expiration_year', None)
        userPaymentMethod = UserPaymentMethod(
                user_id=user_id,
                package_id=package_id,
                card_name=card_name,
                amount=amount,
                card_number=card_number,
                cvc=cvc,
                expiration_month=expiration_month,
                expiration_year=expiration_year,
        )
        userPaymentMethod.save()
        userPaymentMethod.user_payment_id = userPaymentMethod.pk
        userPaymentMethod.save()
        data['user_payment_id'] =  userPaymentMethod.pk
        return data

    def update(self, instance, data):
        instance.user_payment_id = data.get('user_payment_id',
        instance.user_payment_id)
        instance.user_id = data.get('user_id',
        instance.user_id)
        instance.package_id = data.get('package_id',
        instance.package_id)
        instance.card_name = data.get('card_name',
        instance.card_name)
        instance.cvc = data.get('cvc',
        instance.cvc)
        instance.expiration_month = data.get('expiration_month',
        instance.expiration_month)
        instance.expiration_year = data.get('expiration_year',
        instance.expiration_date)
        instance.save()


# Payment Method options
class PaymentMethodSerializer(serializers.ModelSerializer):
        class Meta:
            model = PaymentMethod
            fields = ['__all__']

        def create(self, data):
            payment_method_name = data.get('payment_method_name', None)
            payment_method_currency = data.get('payment_method_currency', None)
            payment_method_public_key = data.get('payment_method_public_key', None)
            payment_method_secret_key = data.get('payment_method_secret_key', None)
            payment_method_status = data.get('payment_method_status', False)
            paymentMethod = PaymentMethod(
                payment_method_name=payment_method_name,
                payment_method_currency=payment_method_currency,
                payment_method_public_key=payment_method_public_key,
                payment_method_secret_key=payment_method_secret_key,
                payment_method_status=payment_method_status,
            )

            paymentMethod.save()
            paymentMethod.payment_method_id = paymentMethod.pk
            paymentMethod.save()
            data['payment_method_id'] = paymentMethod.pk
            return data

        def update(self, instance, data):
            instance.payment_method_name = data.get('payment_method_name', instance.payment_method_name)
            instance.payment_method_currency = data.get('payment_method_currency', instance.payment_method_currency)
            instance.payment_method_public_key = data.get('payment_method_public_key', instance.payment_method_public_key)
            instance.payment_method_secret_key = data.get('payment_method_secret_key', instance.payment_method_secret_key)
            instance.payment_method_status = data.get('payment_method_status', instance.payment_method_status)
            instance.save()


# Notification Settings Serializer

class NotificationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSettings
        fields = ['__all__']

    def create(self, data):
        settings_name = data.get('settings_name', None)
        settings_value = data.get('settings_value', None)
        settings_status = data.get('settings_status', True)
        notificationSettings = NotificationSettings(
            settings_name=settings_name,
            settings_value=settings_value,
            settings_status=settings_status
        )

        notificationSettings.save()
        notificationSettings.notification_id = notificationSettings.pk
        notificationSettings.save()

        data['notification_id'] = notificationSettings.pk
        return data


    def update(self, instance, data):
        instance.settings_name = data.get('settings_name', instance.settings_name)
        instance.settings_value = data.get('settings_value', instance.settings_value)
        instance.settings_status = data.get('settings_status', instance.settings_status)
        instance.save()


# PackageSettings Serializer
class PackageSettingsSerializer(serializers.ModelSerializer):
        class Meta:
            model= PackageSettings
        def create(self, data):
            package_name = data.get('package_name', None)
            package_duration = data.get('package_duration', None)
            package_price = data.get('package_price', None)
            package_status = data.get('package_status', True)
            package_note = data.get('package_note', None)
            packageSettings = PackageSettings(
                package_name=package_name,
                package_duration=package_duration,
                package_price=package_price,
                package_status=package_status,
                package_note=package_note
            )
            packageSettings.save()
            packageSettings.package_id = packageSettings.pk
            packageSettings.save()

        def update(self, instance, data):
            instance.package_name = data.get('package_name', instance.package_name)
            instance.package_duration = data.get('package_duration', instance.package_duration)
            instance.package_price = data.get('package_price', instance.package_duration)
            instance.package_status = data.get('package_status', instance.package_status)
            instance.package_note = data.get('package_note', instance.package_note)
            instance.save()





