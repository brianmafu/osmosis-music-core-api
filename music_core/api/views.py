# Music API Generic API Views

from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)
from django.db.models import Q
from rest_framework import pagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, IsAuthenticated)
from  music_core.api.serializers import PlaylistSerializer, ArtistSerializer, SongSerializer, VideoSerializer
from music_core.models import Artist, Song, Playlist, Video
from rest_framework.pagination import LimitOffsetPagination

# Playlist Views
class PlaylistListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PlaylistSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Playlist.objects.all()
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


class PlaylistCreateAPIView(CreateAPIView):
    serializer_class = PlaylistSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Playlist.objects.all()


class PlaylistDetailAPIView(RetrieveAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistDeleteAPIView(DestroyAPIView):
    queryset = Playlist.objects.all()
    #permission_classes = [IsAuthenticated]
    serializer_class = PlaylistSerializer


class PlaylistUpdateAPIView(RetrieveUpdateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

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
                Q(email__icontains=query) |
                Q(title_icontains=query) |
                Q(name__icontains=query) |
                Q(phone__icontains=query)


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
        queryset_list = Artist.objects.all()
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

