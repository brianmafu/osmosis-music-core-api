from rest_framework.serializers import ModelSerializer

from music_core.models import (Admin, AdsSettings, Album, ApiList,
                               ApiListParameters, Artist, BannerSlider,
                               Category, HomeComponents, Liked, Movie, Music,
                               NotificationSettings, PackageSettings,
                               PaymentMethod, RecentlyView, SettingsFlag, User,
                               UserPayment, UserPlaylist, UserPlaylistMusic)


class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class AdsSettingsSerializer(ModelSerializer):
    class Meta:
        model = AdsSettings
        fields = "__all__"


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class ApiListSerializer(ModelSerializer):
    class Meta:
        model = ApiList
        fields = "__all__"


class ApiListParametersSerializer(ModelSerializer):
    class Meta:
        model = ApiListParameters
        fields = "__all__"


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class BannerSliderSerializer(ModelSerializer):
    class Meta:
        model = BannerSlider
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class HomeComponentsSerializer(ModelSerializer):
    class Meta:
        model = HomeComponents
        fields = "__all__"


class LikedSerializer(ModelSerializer):
    class Meta:
        model = Liked
        fields = "__all__"


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MusicSerializer(ModelSerializer):
    class Meta:
        model = Music
        fields = "__all__"


class NotificationSettingsSerializer(ModelSerializer):
    class Meta:
        model = NotificationSettings
        fields = "__all__"


class PackageSettingsSerializer(ModelSerializer):
    class Meta:
        model = PackageSettings
        fields = "__all__"


class PaymentMethodSerializer(ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class RecentlyViewSerializer(ModelSerializer):
    class Meta:
        model = RecentlyView
        fields = "__all__"


class SettingsFlagSerializer(ModelSerializer):
    class Meta:
        model = SettingsFlag
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserPaymentSerializer(ModelSerializer):
    class Meta:
        model = UserPayment
        fields = "__all__"


class UserPlaylistSerializer(ModelSerializer):
    class Meta:
        model = UserPlaylist
        fields = "__all__"


class UserPlaylistMusicSerializer(ModelSerializer):
    class Meta:
        model = UserPlaylistMusic
        fields = "__all__"
