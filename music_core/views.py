from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from music_core.serializers import AdminSerializer, AdsSettingsSerializer, AlbumSerializer, ApiListSerializer, ApiListParametersSerializer, ArtistSerializer, BannerSliderSerializer, CategorySerializer, HomeComponentsSerializer, LikedSerializer, MovieSerializer, MusicSerializer, NotificationSettingsSerializer, PackageSettingsSerializer, PaymentMethodSerializer, RecentlyViewSerializer, SettingsFlagSerializer, UserSerializer, UserPaymentSerializer, UserPlaylistSerializer, UserPlaylistMusicSerializer
from music_core.models import Admin, AdsSettings, Album, ApiList, ApiListParameters, Artist, BannerSlider, Category, HomeComponents, Liked, Movie, Music, NotificationSettings, PackageSettings, PaymentMethod, RecentlyView, SettingsFlag, User, UserPayment, UserPlaylist, UserPlaylistMusic


class AdminViewSet(ViewSet):

    def list(self, request):
        queryset = Admin.objects.order_by('pk')
        serializer = AdminSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Admin.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AdminSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Admin.objects.get(pk=pk)
        except Admin.DoesNotExist:
            return Response(status=404)
        serializer = AdminSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Admin.objects.get(pk=pk)
        except Admin.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AdsSettingsViewSet(ViewSet):

    def list(self, request):
        queryset = AdsSettings.objects.order_by('pk')
        serializer = AdsSettingsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AdsSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AdsSettings.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AdsSettingsSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AdsSettings.objects.get(pk=pk)
        except AdsSettings.DoesNotExist:
            return Response(status=404)
        serializer = AdsSettingsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AdsSettings.objects.get(pk=pk)
        except AdsSettings.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AlbumViewSet(ViewSet):

    def list(self, request):
        queryset = Album.objects.order_by('pk')
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Album.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AlbumSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            return Response(status=404)
        serializer = AlbumSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ApiListViewSet(ViewSet):

    def list(self, request):
        queryset = ApiList.objects.order_by('pk')
        serializer = ApiListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ApiListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = ApiList.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ApiListSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = ApiList.objects.get(pk=pk)
        except ApiList.DoesNotExist:
            return Response(status=404)
        serializer = ApiListSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = ApiList.objects.get(pk=pk)
        except ApiList.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ApiListParametersViewSet(ViewSet):

    def list(self, request):
        queryset = ApiListParameters.objects.order_by('pk')
        serializer = ApiListParametersSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ApiListParametersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = ApiListParameters.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ApiListParametersSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = ApiListParameters.objects.get(pk=pk)
        except ApiListParameters.DoesNotExist:
            return Response(status=404)
        serializer = ApiListParametersSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = ApiListParameters.objects.get(pk=pk)
        except ApiListParameters.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ArtistViewSet(ViewSet):

    def list(self, request):
        queryset = Artist.objects.order_by('pk')
        serializer = ArtistSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Artist.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ArtistSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            return Response(status=404)
        serializer = ArtistSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class BannerSliderViewSet(ViewSet):

    def list(self, request):
        queryset = BannerSlider.objects.order_by('pk')
        serializer = BannerSliderSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BannerSliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = BannerSlider.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = BannerSliderSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = BannerSlider.objects.get(pk=pk)
        except BannerSlider.DoesNotExist:
            return Response(status=404)
        serializer = BannerSliderSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = BannerSlider.objects.get(pk=pk)
        except BannerSlider.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CategoryViewSet(ViewSet):

    def list(self, request):
        queryset = Category.objects.order_by('pk')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class HomeComponentsViewSet(ViewSet):

    def list(self, request):
        queryset = HomeComponents.objects.order_by('pk')
        serializer = HomeComponentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HomeComponentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = HomeComponents.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = HomeComponentsSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = HomeComponents.objects.get(pk=pk)
        except HomeComponents.DoesNotExist:
            return Response(status=404)
        serializer = HomeComponentsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = HomeComponents.objects.get(pk=pk)
        except HomeComponents.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class LikedViewSet(ViewSet):

    def list(self, request):
        queryset = Liked.objects.order_by('pk')
        serializer = LikedSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LikedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Liked.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = LikedSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Liked.objects.get(pk=pk)
        except Liked.DoesNotExist:
            return Response(status=404)
        serializer = LikedSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Liked.objects.get(pk=pk)
        except Liked.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class MovieViewSet(ViewSet):

    def list(self, request):
        queryset = Movie.objects.order_by('pk')
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = MovieSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=404)
        serializer = MovieSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class MusicViewSet(ViewSet):

    def list(self, request):
        queryset = Music.objects.order_by('pk')
        serializer = MusicSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Music.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = MusicSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            return Response(status=404)
        serializer = MusicSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class NotificationSettingsViewSet(ViewSet):

    def list(self, request):
        queryset = NotificationSettings.objects.order_by('pk')
        serializer = NotificationSettingsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NotificationSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = NotificationSettings.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = NotificationSettingsSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = NotificationSettings.objects.get(pk=pk)
        except NotificationSettings.DoesNotExist:
            return Response(status=404)
        serializer = NotificationSettingsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = NotificationSettings.objects.get(pk=pk)
        except NotificationSettings.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PackageSettingsViewSet(ViewSet):

    def list(self, request):
        queryset = PackageSettings.objects.order_by('pk')
        serializer = PackageSettingsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PackageSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = PackageSettings.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PackageSettingsSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = PackageSettings.objects.get(pk=pk)
        except PackageSettings.DoesNotExist:
            return Response(status=404)
        serializer = PackageSettingsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = PackageSettings.objects.get(pk=pk)
        except PackageSettings.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PaymentMethodViewSet(ViewSet):

    def list(self, request):
        queryset = PaymentMethod.objects.order_by('pk')
        serializer = PaymentMethodSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = PaymentMethod.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PaymentMethodSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = PaymentMethod.objects.get(pk=pk)
        except PaymentMethod.DoesNotExist:
            return Response(status=404)
        serializer = PaymentMethodSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = PaymentMethod.objects.get(pk=pk)
        except PaymentMethod.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RecentlyViewViewSet(ViewSet):

    def list(self, request):
        queryset = RecentlyView.objects.order_by('pk')
        serializer = RecentlyViewSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RecentlyViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = RecentlyView.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = RecentlyViewSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = RecentlyView.objects.get(pk=pk)
        except RecentlyView.DoesNotExist:
            return Response(status=404)
        serializer = RecentlyViewSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = RecentlyView.objects.get(pk=pk)
        except RecentlyView.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SettingsFlagViewSet(ViewSet):

    def list(self, request):
        queryset = SettingsFlag.objects.order_by('pk')
        serializer = SettingsFlagSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SettingsFlagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = SettingsFlag.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = SettingsFlagSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = SettingsFlag.objects.get(pk=pk)
        except SettingsFlag.DoesNotExist:
            return Response(status=404)
        serializer = SettingsFlagSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = SettingsFlag.objects.get(pk=pk)
        except SettingsFlag.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserViewSet(ViewSet):

    def list(self, request):
        queryset = User.objects.order_by('pk')
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        serializer = UserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserPaymentViewSet(ViewSet):

    def list(self, request):
        queryset = UserPayment.objects.order_by('pk')
        serializer = UserPaymentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserPaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = UserPayment.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserPaymentSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = UserPayment.objects.get(pk=pk)
        except UserPayment.DoesNotExist:
            return Response(status=404)
        serializer = UserPaymentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = UserPayment.objects.get(pk=pk)
        except UserPayment.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserPlaylistViewSet(ViewSet):

    def list(self, request):
        queryset = UserPlaylist.objects.order_by('pk')
        serializer = UserPlaylistSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserPlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = UserPlaylist.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserPlaylistSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = UserPlaylist.objects.get(pk=pk)
        except UserPlaylist.DoesNotExist:
            return Response(status=404)
        serializer = UserPlaylistSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = UserPlaylist.objects.get(pk=pk)
        except UserPlaylist.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserPlaylistMusicViewSet(ViewSet):

    def list(self, request):
        queryset = UserPlaylistMusic.objects.order_by('pk')
        serializer = UserPlaylistMusicSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserPlaylistMusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = UserPlaylistMusic.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserPlaylistMusicSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = UserPlaylistMusic.objects.get(pk=pk)
        except UserPlaylistMusic.DoesNotExist:
            return Response(status=404)
        serializer = UserPlaylistMusicSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = UserPlaylistMusic.objects.get(pk=pk)
        except UserPlaylistMusic.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
