from django.conf.urls import url
from .views  import (
    ArtistListAPIView, ArtistDetailAPIView, ArtistCreateAPIView, ArtistDeleteAPIView, ArtistUpdateAPIView,
    AlbumListAPIView, AlbumDetailAPIView, AlbumCreateAPIView, AlbumDeleteAPIView, AlbumUpdateAPIView,
    PlaylistListAPIView, PlaylistDetailAPIView, PlaylistCreateAPIView, PlaylistDeleteAPIView, PlaylistUpdateAPIView,
    SongListAPIView, SongDetailAPIView, SongCreateAPIView, SongDeleteAPIView, SongUpdateAPIView,
    VideoListAPIView, VideoDetailAPIView, VideoCreateAPIView, VideoDeleteAPIView, VideoUpdateAPIView,
    
)
urlpatterns = [
    url(r'^artists', ArtistListAPIView.as_view(), name='Artists'),
    url(r'^artist-create', ArtistCreateAPIView.as_view(), name='Artist-Create'),
    url(r'^artist-datails/<int:pk>/', ArtistDetailAPIView.as_view(), name='Artist-Details'),
    url(r'^artist-delete/<int:pk>/', ArtistDeleteAPIView.as_view(), name='Artist-Delete'),
    url(r'^artist-update/<int:pk>/', ArtistUpdateAPIView.as_view(), name='Artist-Update'),

    url(r'^playlists', PlaylistListAPIView.as_view(), name='Playlists'),
    url(r'^playlist-create', PlaylistCreateAPIView.as_view(), name='Playlist-Create'),
    url(r'^playlist-datails/<int:pk>/', PlaylistDetailAPIView.as_view(), name='Playlist-Details'),
    url(r'^playlist-delete/<int:pk>/', PlaylistDeleteAPIView.as_view(), name='Playlist-Delete'),
    url(r'^playlist-update/<int:pk>/', PlaylistUpdateAPIView.as_view(), name='Playlist-Update'),

    url(r'^songs', SongListAPIView.as_view(), name='Songs'),
    url(r'^song-create', SongCreateAPIView.as_view(), name='Song-Create'),
    url(r'^song-datails/<int:pk>/', SongDetailAPIView.as_view(), name='Song-Details'),
    url(r'^song-delete/<int:pk>/', SongDeleteAPIView.as_view(), name='Song-Delete'),
    url(r'^song-update/<int:pk>/', SongUpdateAPIView.as_view(), name='Song-Update'),



    url(r'^album', AlbumListAPIView.as_view(), name='Albums'),
    url(r'^album-create', AlbumCreateAPIView.as_view(), name='Album-Create'),
    url(r'^album-datails/<int:pk>/', AlbumDetailAPIView.as_view(), name='Album-Details'),
    url(r'^album-delete/<int:pk>/', AlbumDeleteAPIView.as_view(), name='Album-Delete'),
    url(r'^album-update/<int:pk>/', AlbumUpdateAPIView.as_view(), name='Album-Update'),


    url(r'^videos', VideoListAPIView.as_view(), name='Videos'),
    url(r'^video-create', VideoCreateAPIView.as_view(), name='Video-Create'),
    url(r'^video-datails/<int:pk>/', VideoDetailAPIView.as_view(), name='Video-Details'),
    url(r'^video-delete/<int:pk>/', VideoDeleteAPIView.as_view(), name='Video-Delete'),
    url(r'^video-update/<int:pk>/', VideoUpdateAPIView.as_view(), name='Video-Update'),




    # url(r'^playlists', views.playlists, name='Playlist'),

    # url(r'^songs', views.songs, name='Songs'),

    # url(r'^404/', views.error_404, name="404")
]
