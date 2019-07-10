from django.conf.urls import url
from .views  import (
    ArtistListAPIView, ArtistDetailAPIView, ArtistCreateAPIView, ArtistDeleteAPIView, ArtistUpdateAPIView
)
urlpatterns = [
    # url(r'^playlist/(?P<name>\D+)/',
    #     views.songs_per_playlist,
    #     name='playlist songs'),

    # url(r'^artists/(?P<name>\D+)/',
    #     views.songs_per_artist,
    #     name='artist songs'),

    url(r'^artists', ArtistListAPIView.as_view(), name='Artists'),

    # url(r'^playlists', views.playlists, name='Playlist'),

    # url(r'^songs', views.songs, name='Songs'),

    # url(r'^404/', views.error_404, name="404")
]
