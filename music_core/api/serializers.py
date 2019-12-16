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
        title = data.get('title', None)
        artist_id = data.get('artist_id', 1)
        genre = data.get('genre', "Unknown")
        print("genre: {}".format(genre))
        language=data.get('language', None)
        stars = data.get('stars', 0)
        thumbnail = data.get('thumbnail', None) 
        duration = data.get('duration', 0)
        artist = Artist.objects.filter(id=int(artist_id))
        artist = artist[0] if artist else None
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

