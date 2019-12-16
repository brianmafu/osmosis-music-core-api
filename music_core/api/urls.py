from django.conf.urls import url
from django.urls import path


from .views  import (
    ArtistListAPIView, ArtistDetailAPIView, ArtistCreateAPIView, ArtistDeleteAPIView, ArtistUpdateAPIView,
    AlbumListAPIView, AlbumDetailAPIView, AlbumCreateAPIView, AlbumDeleteAPIView, AlbumUpdateAPIView,AlbumSearchAPIView,
    PlaylistListAPIView, PlaylistDetailAPIView, PlaylistCreateAPIView, PlaylistDeleteAPIView, PlaylistUpdateAPIView,
    SongListAPIView, SongDetailAPIView, SongCreateAPIView, SongDeleteAPIView, SongUpdateAPIView,
    VideoListAPIView, VideoDetailAPIView, VideoCreateAPIView, VideoDeleteAPIView, VideoUpdateAPIView, getHome,
    getGenres
)
urlpatterns = [

    # Home Views

    path('home', getHome),
    path('categories', getGenres),

    path('artists', ArtistListAPIView.as_view(), name='Artists'),
    path('artist-create', ArtistCreateAPIView.as_view(), name='Artist-Create'),
    path('artist-details/<int:pk>/', ArtistDetailAPIView.as_view(), name='Artist-Details'),
    path('artist-delete/<int:pk>/', ArtistDeleteAPIView.as_view(), name='Artist-Delete'),
    path('artist-update/<int:pk>/', ArtistUpdateAPIView.as_view(), name='Artist-Update'),

    path('playlists', PlaylistListAPIView.as_view(), name='Playlists'),
    path('playlist-create', PlaylistCreateAPIView.as_view(), name='Playlist-Create'),
    path('playlist-details/<int:pk>/', PlaylistDetailAPIView.as_view(), name='Playlist-Details'),
    path('playlist-delete/<int:pk>/', PlaylistDeleteAPIView.as_view(), name='Playlist-Delete'),
    path('playlist-update/<int:pk>/', PlaylistUpdateAPIView.as_view(), name='Playlist-Update'),

    path('songs', SongListAPIView.as_view(), name='Songs'),
    path('song-create', SongCreateAPIView.as_view(), name='Song-Create'),
    path('song-details/<int:pk>/', SongDetailAPIView.as_view(), name='Song-Details'),
    path('song-delete/<int:pk>/', SongDeleteAPIView.as_view(), name='Song-Delete'),
    path('song-update/<int:pk>/', SongUpdateAPIView.as_view(), name='Song-Update'),


    path('albums', AlbumListAPIView.as_view(), name='Albums'),
    path('albums-search', AlbumSearchAPIView.as_view(), name='Albums-Search'),
    path('album-create', AlbumCreateAPIView.as_view(), name='Album-Create'),
    path('album-details/<int:pk>/', AlbumDetailAPIView.as_view(), name='Album-Details'),
    path('album-delete/<int:pk>/', AlbumDeleteAPIView.as_view(), name='Album-Delete'),
    path('album-update/<int:pk>/', AlbumUpdateAPIView.as_view(), name='Album-Update'),


    path('videos', VideoListAPIView.as_view(), name='Videos'),
    path('video-create', VideoCreateAPIView.as_view(), name='Video-Create'),
    path('video-details/<int:pk>/', VideoDetailAPIView.as_view(), name='Video-Details'),
    path('video-delete/<int:pk>/', VideoDeleteAPIView.as_view(), name='Video-Delete'),
    path('video-update/<int:pk>/', VideoUpdateAPIView.as_view(), name='Video-Update'),
]
