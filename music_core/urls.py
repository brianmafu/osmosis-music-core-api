from rest_framework.routers import SimpleRouter
from music_core import views


router = SimpleRouter()

router.register(r'admin', views.AdminViewSet, 'Admin')
router.register(r'adssettings', views.AdsSettingsViewSet, 'AdsSettings')
router.register(r'album', views.AlbumViewSet, 'Album')
router.register(r'apilist', views.ApiListViewSet, 'ApiList')
router.register(r'apilistparameters', views.ApiListParametersViewSet, 'ApiListParameters')
router.register(r'artist', views.ArtistViewSet, 'Artist')
router.register(r'bannerslider', views.BannerSliderViewSet, 'BannerSlider')
router.register(r'category', views.CategoryViewSet, 'Category')
router.register(r'homecomponents', views.HomeComponentsViewSet, 'HomeComponents')
router.register(r'liked', views.LikedViewSet, 'Liked')
router.register(r'movie', views.MovieViewSet, 'Movie')
router.register(r'music', views.MusicViewSet, 'Music')
router.register(r'notificationsettings', views.NotificationSettingsViewSet, 'NotificationSettings')
router.register(r'packagesettings', views.PackageSettingsViewSet, 'PackageSettings')
router.register(r'paymentmethod', views.PaymentMethodViewSet, 'PaymentMethod')
router.register(r'recentlyview', views.RecentlyViewViewSet, 'RecentlyView')
router.register(r'settingsflag', views.SettingsFlagViewSet, 'SettingsFlag')
router.register(r'user', views.UserViewSet, 'User')
router.register(r'userpayment', views.UserPaymentViewSet, 'UserPayment')
router.register(r'userplaylist', views.UserPlaylistViewSet, 'UserPlaylist')
router.register(r'userplaylistmusic', views.UserPlaylistMusicViewSet, 'UserPlaylistMusic')

urlpatterns = router.urls
