# Music API Generic API Views

from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)
from django.db.models import Q
from rest_framework import pagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, IsAuthenticated)
from  music_core.api.serializers import UserPlaylistSerializer, UserPlaylistMusicSerializer, \
    ArtistSerializer, SongSerializer, \
    VideoSerializer, AlbumSerializer, \
    UserPaymentMethodSerializer, PaymentMethodSerializer, \
    NotificationSettingsSerializer, PackageSettingsSerializer, \
    CategorySerializer, HomeComponentSerializer
from music_core.models import Artist, Song,\
    UserPlaylist, Video, \
    Album, UserPlaylistMusic,\
    UserPaymentMethod, PaymentMethod, \
    NotificationSettings, PackageSettings, Category, HomeComponent
from rest_framework.pagination import LimitOffsetPagination
from django.core import serializers
from django.http import HttpResponse
import json
import requests


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

# Playlist Views
class UserPlaylistListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserPlaylistSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = UserPlaylist.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(title_icontains=query) |
                Q(name__icontains=query) |
                Q(phone__icontains=query)


            )

        return queryset_list.order_by('-id')


# UserPlaylist View
class UserPlaylistCreateAPIView(CreateAPIView):
    serializer_class = UserPlaylistSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserPlaylist.objects.all()


class UserPlaylistDetailAPIView(RetrieveAPIView):
    queryset = UserPlaylist.objects.all()
    serializer_class = UserPlaylistSerializer


class UserPlaylistDeleteAPIView(DestroyAPIView):
    queryset = UserPlaylist.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = UserPlaylistSerializer


class UserPlaylistUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserPlaylist.objects.all()
    serializer_class = UserPlaylistSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



# UserPlaylist Music /Song Views
class UserPlaylistMusicListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserPlaylistMusicSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = UserPlaylistMusic.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(title_icontains=query) |
                Q(name__icontains=query) |
                Q(phone__icontains=query)


            )

        return queryset_list.order_by('-id')

class UserPlaylistMusicCreateAPIView(CreateAPIView):
    serializer_class = UserPlaylistMusicSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserPlaylistMusic.objects.all()


class UserPlaylistMusicDetailAPIView(RetrieveAPIView):
    queryset = UserPlaylistMusic.objects.all()
    serializer_class = UserPlaylistMusicSerializer


class UserPlaylistMusicDeleteAPIView(DestroyAPIView):
    queryset = UserPlaylistMusic.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = UserPlaylistMusicSerializer


class UserPlaylistMusicUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserPlaylistMusic.objects.all()
    serializer_class = UserPlaylistMusicSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



# UserPaymentMethod views

class UserPaymentMethodListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserPaymentMethodSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = UserPaymentMethod.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(title_icontains=query) |
                Q(name__icontains=query) |
                Q(phone__icontains=query)


            )

        return queryset_list.order_by('-id')
class UserPaymentMethodCreateAPIView(CreateAPIView):
    serializer_class = UserPaymentMethodSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserPaymentMethod.objects.all()


class UserPaymentMethodDetailAPIView(RetrieveAPIView):
    queryset = UserPaymentMethod.objects.all()
    serializer_class = UserPaymentMethodSerializer


class UserPaymentMethodDeleteAPIView(DestroyAPIView):
    queryset = UserPaymentMethod.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = UserPaymentMethodSerializer


# PaymentMethod Option Views
class PaymentMethodListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PaymentMethodSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = PaymentMethod.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(title_icontains=query) |
                Q(name__icontains=query) |
                Q(phone__icontains=query)


            )

        return queryset_list.order_by('-id')
class PaymentMethodCreateAPIView(CreateAPIView):
    serializer_class = PaymentMethodSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = PaymentMethod.objects.all()


class PaymentMethodDetailAPIView(RetrieveAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class  PaymentMethodDeleteAPIView(DestroyAPIView):
    queryset = UserPaymentMethod.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = PaymentMethodSerializer


2# NotificationSettings Views
class NotificationSettingsListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = NotificationSettingsSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = NotificationSettings.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(title_icontains=query) |
                Q(name__icontains=query) |
                Q(phone__icontains=query)


            )

        return queryset_list.order_by('-id')
class NotificationSettingsCreateAPIView(CreateAPIView):
    serializer_class = NotificationSettingsSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = NotificationSettings.objects.all()


class NotificationSettingsDetailAPIView(RetrieveAPIView):
    queryset = NotificationSettings.objects.all()
    serializer_class = NotificationSettingsSerializer


class  NotificationSettingsDeleteAPIView(DestroyAPIView):
    queryset = NotificationSettings.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = NotificationSettingsSerializer

class NotificationsUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = NotificationSettings.objects.all()
    serializer_class = NotificationSettingsSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



#PackageSettings view
class PackageSettingsListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PackageSettingsSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = PackageSettings.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(title_icontains=query) |
                Q(name__icontains=query) |
                Q(phone__icontains=query)


            )

        return queryset_list.order_by('-id')
class PackageSettingsCreateAPIView(CreateAPIView):
    serializer_class = PackageSettingsSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = PackageSettings.objects.all()


class PackageSettingsAPIView(RetrieveAPIView):
    queryset = PackageSettings.objects.all()
    serializer_class = PackageSettingsSerializer


class  PackageSettingsDeleteAPIView(DestroyAPIView):
    queryset = PackageSettings.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = PackageSettingsSerializer

class PackageSettingsUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = PackageSettings.objects.all()
    serializer_class = PackageSettingsSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PackageSettingsUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = PackageSettings.objects.all()
    serializer_class = PackageSettingsSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Artist Views
class ArtistListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ArtistSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Artist.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title_icontains=query) 


            )

        return queryset_list.order_by('-id')

class ArtistCreateAPIView(CreateAPIView):
    serializer_class = ArtistSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Artist.objects.all()


class ArtistDetailAPIView(RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDeleteAPIView(DestroyAPIView):
    queryset = Artist.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = ArtistSerializer


class ArtistUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# Song Views
class SongListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Song.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(artist__icontains=query) |
                Q(title_icontains=query)
            )

        return queryset_list.order_by('-id')


class SongCreateAPIView(CreateAPIView):
    serializer_class = SongSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()


class SongDetailAPIView(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDeleteAPIView(DestroyAPIView):
    queryset = Song.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = SongSerializer


class SongUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# Album Views
class AlbumListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AlbumSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Album.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(artist__icontains=query) |
                Q(title_icontains=query)
            )

        return queryset_list.order_by('-id')

class AlbumSearchAPIView(ListAPIView):
    serializer_class = AlbumSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Album.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)
            )

        return queryset_list.order_by('-id')

class AlbumCreateAPIView(CreateAPIView):
    serializer_class = AlbumSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.all()


class AlbumDetailAPIView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDeleteAPIView(DestroyAPIView):
    queryset = Album.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = AlbumSerializer


class AlbumUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# Video Views

class VideoListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = VideoSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Video.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(title_icontains=query) |
                Q(name__icontains=query) |
                Q(phone__icontains=query)


            )

        return queryset_list.order_by('-id')

class VideoCreateAPIView(CreateAPIView):
    serializer_class = VideoSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Video.objects.all()


class VideoDetailAPIView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = SongSerializer


class VideoDeleteAPIView(DestroyAPIView):
    queryset = Video.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = VideoSerializer


class VideoUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# Category Views
class CategoryListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Category.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(title_icontains=query) |
                Q(name__icontains=query) |
                Q(phone__icontains=query)


            )

        return queryset_list.order_by('-id')

class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Video.objects.all()


class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer


class CategoryUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



# Home Component Views
class HomeComponentListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = HomeComponentSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = HomeComponent.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(title_icontains=query) |
                Q(name__icontains=query) |
                Q(phone__icontains=query)


            )

        return queryset_list.order_by('-id')

class HomeComponentCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = HomeComponent.objects.all()


class HomeComponentDetailAPIView(RetrieveAPIView):
    queryset = HomeComponent.objects.all()
    serializer_class = HomeComponentSerializer


class HomeComponentDeleteAPIView(DestroyAPIView):
    queryset = HomeComponent.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = HomeComponentSerializer


class HomeCompoentUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = HomeComponent.objects.all()
    serializer_class = HomeComponentSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

def querySetToJSON(query_set) :
    all_query_set_objects = json.loads(serializers.serialize('json', query_set))
    jsonQuerySet = []
    for objectItem in all_query_set_objects:
        jsonQuerySet.append(objectItem['fields'])
    return jsonQuerySet

def getHome(request):
    trendingArtists = Artist.objects.all()
    newReleases = Album.objects.all().order_by('date_created')
    hottestSongs = Song.objects.all()
    homeData = {
        "trendingArtists":querySetToJSON(trendingArtists),
        "newReleases": querySetToJSON(newReleases),
        "hottestSongs": querySetToJSON(hottestSongs)
    }

    return HttpResponse(json.dumps(homeData), content_type='application/json')


def getGenres(request): 
    # GENRE_BASE_URL = "http://developer.echonest.com/api/v4/artist/list_genres?api_key=YOUR_API_KEY&format=json"
    #response = requests.get(GENRE_BASE_URL)
    

    return HttpResponse(json.dumps([{v[0]: v[1]} for v in GENRE_CHOICES]))


