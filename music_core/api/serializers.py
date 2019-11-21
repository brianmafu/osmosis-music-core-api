from rest_framework import serializers
from music_core.models import Artist, Playlist, Song, Video, Album

# Playlist Serializer
class  PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = [
            'pk',
            'name',
            'cover_art',
        ]
  
    def create(self, data):
        name = data['name']
        cover_art = data['cover_art']

        play_list = Playlist(
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
            'thumbnailProfileImageURL',
            'about',
            'stars'           

        ]
  
    def create(self, data):
        title = data['title']
        first_name = data['first_name']
        last_name = data['last_name']
        language = data['language']
        name = data['name']
        profileImageURL = data['profileImageURL']
        thumbnailProfileImageURL = data['thumbnailProfileImageURL']
        about = data['about']
        stars = data['stars']

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
        ]
  
    def create(self, data):
        title = data['title']
        artist_id = data['artist_id'] or -1
        genre = data['genre']
        language=data['language']
        stars = data['stars']
        genre=data['genre']
        thumbnail=data['thumbnail']
        duration = data['duration']
        artist = Artist.objects.filter(id=artist_id)[:1]
        album = Album(
            title=title,
            artist=artist or None,
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
        artist = Artist.objects.filter(id=int(data.get('artist_id', -1)))[:1]
        album = Album.objects.filter(id=int(data.get('album_id', -1)))[:1]
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
        title = data['title']
        artist_id=data['artist_id'] or -1
        genre=data['genre']
        stars = data['stars']
        language=data['language']
        imageURL=data['imageURL']
        fileName=data['fileName']
        thumbnailImageURL=data['thumbnailImageURL']
        album_id=data['album_id'] or -1
        duration=data['duration']
        description=data['description']
        durationInSeconds=data['durationInSeconds']
        album=Album.objects.filter(id=int(album_id))[0] or None
        artist=Artist.objects.filter(id=artist_id)[:1]
        song = Song(
            title=title,
            artist=artist or None,
            genre=genre,
            imageURL=imageURL,
            thumbnailImageURL = thumbnailImageURL,
            album=album or None,
            language=language,
            stars=stars,
            duration=duration,
            description=description,
            durationInSeconds=durationInSeconds,
            fileName=fileName
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
        artist = Artist.objects.filter(id=int(data.get('artist_id', -1)))[:1]
        album = Album.objects.filter(id=int(data.get('album_id', -1)))[0]
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
        title = data['title']
        url = data['url']
        genre = data['genre']
        artist_id = data['artist_id'] or -1
        artist = Artist.objects.filter(id=int(artist_id))[0]
        language = data['language']
        thumbnail = data['thumbnail']

        video = Video(
            title=title,
            url=url,
            artist=artist,
            language=language,
            image=image
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

