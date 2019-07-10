from rest_framework import serializers
from music_core.models import Artist, Playlist, Song, Video

# Playlist Serializer
class  PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = [
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
            'first_name',
            'last_name',
            'image',
            'language',
        ]
  
    def create(self, data):
        first_name = data['first_name']
        last_name = data['last_name']
        image = data['image']
        language = data['language']

        artist = Artist(
            first_name=first_name,
            last_name=last_name,
            image=image,
            language=language,
        )
        artist.save()
        data['id'] =  artist.id
        return data

    def update(self, instance, data):
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.image = data.get('image', instance.image)
        instance.language = data.get('language', instance.language)
        instance.save()


# Song Serializer
class  SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            'title',
            'artist',
            'url',
            'play_list',
            'genre',
            'language',
        ]
  
    def create(self, data):
        title = data['title']
        artist_id = data['artist_id'] or -1
        url = data['url']
        play_list_id = data['play_list_id'] or -1
        genre = data['genre']
        language=data['language']
        artist = Artist.objects.filter(id=artist_id)[0]
        play_list = Playlist.objects.filter(id=play_list_id)[0]
        song = Song(
            title=title,
            artist=artist or None,
            url=url,
            genre=genre,
            play_list=play_list or None,
            language=language

        )
        song.save()
        data['id'] =  song.id
        return data

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.url = data.get('url', instance.url)
        instance.language = data.get('language', instance.language)
        instance.genre = data.get('genre', instance.genre)
        artist = Artist.objects.filter(id=int(data.get('artist_id', -1)))[0]
        play_list = Playlist.objects.filter(id=int(data.get('play_list_id', -1)))[0]
        instance.artist = artist or None
        instance.play_list = play_list or None
        instance.save()


# Video Serializer
class  VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
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
        image = data['image']

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
        artist = Artist.objects.filter(id=int(data.get('artist_id', -1)))[0]
        instance.artist = artist or None
        instance.language = data.get('language', instance.language)
        instance.image = data.get('image', instance.image)
        instance.save()

