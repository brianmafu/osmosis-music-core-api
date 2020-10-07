from rest_framework.decorators import api_view
from rest_framework.response import Response
from music_core.models import Admin, AdsSettings, Album, ApiList, ApiListParameters, Artist, BannerSlider, Category, HomeComponents, Liked, Movie, Music, NotificationSettings, PackageSettings, PaymentMethod, RecentlyView, SettingsFlag, User, UserPayment, UserPlaylist, UserPlaylistMusic
from music_core.serializers import AdminSerializer, AdsSettingsSerializer, AlbumSerializer, ApiListSerializer, ApiListParametersSerializer, ArtistSerializer, BannerSliderSerializer, CategorySerializer, HomeComponentsSerializer, LikedSerializer, MovieSerializer, MusicSerializer, NotificationSettingsSerializer, PackageSettingsSerializer, PaymentMethodSerializer, RecentlyViewSerializer, SettingsFlagSerializer, UserSerializer, UserPaymentSerializer, UserPlaylistSerializer, UserPlaylistMusicSerializer


@api_view(['GET', 'POST'])
def admin_list(request):
    if request.method == 'GET':
        items = Admin.objects.order_by('pk')
        serializer = AdminSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def admin_detail(request, pk):
    try:
        item = Admin.objects.get(pk=pk)
    except Admin.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AdminSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdminSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def adssettings_list(request):
    if request.method == 'GET':
        items = AdsSettings.objects.order_by('pk')
        serializer = AdsSettingsSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdsSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def adssettings_detail(request, pk):
    try:
        item = AdsSettings.objects.get(pk=pk)
    except AdsSettings.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AdsSettingsSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdsSettingsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def album_list(request):
    if request.method == 'GET':
        items = Album.objects.order_by('pk')
        serializer = AlbumSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def album_detail(request, pk):
    try:
        item = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AlbumSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlbumSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def apilist_list(request):
    if request.method == 'GET':
        items = ApiList.objects.order_by('pk')
        serializer = ApiListSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApiListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def apilist_detail(request, pk):
    try:
        item = ApiList.objects.get(pk=pk)
    except ApiList.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ApiListSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApiListSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def apilistparameters_list(request):
    if request.method == 'GET':
        items = ApiListParameters.objects.order_by('pk')
        serializer = ApiListParametersSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApiListParametersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def apilistparameters_detail(request, pk):
    try:
        item = ApiListParameters.objects.get(pk=pk)
    except ApiListParameters.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ApiListParametersSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApiListParametersSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def artist_list(request):
    if request.method == 'GET':
        items = Artist.objects.order_by('pk')
        serializer = ArtistSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail(request, pk):
    try:
        item = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ArtistSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def bannerslider_list(request):
    if request.method == 'GET':
        items = BannerSlider.objects.order_by('pk')
        serializer = BannerSliderSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BannerSliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def bannerslider_detail(request, pk):
    try:
        item = BannerSlider.objects.get(pk=pk)
    except BannerSlider.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = BannerSliderSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BannerSliderSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        items = Category.objects.order_by('pk')
        serializer = CategorySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        item = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def homecomponents_list(request):
    if request.method == 'GET':
        items = HomeComponents.objects.order_by('pk')
        serializer = HomeComponentsSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HomeComponentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def homecomponents_detail(request, pk):
    try:
        item = HomeComponents.objects.get(pk=pk)
    except HomeComponents.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = HomeComponentsSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HomeComponentsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def liked_list(request):
    if request.method == 'GET':
        items = Liked.objects.order_by('pk')
        serializer = LikedSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LikedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def liked_detail(request, pk):
    try:
        item = Liked.objects.get(pk=pk)
    except Liked.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = LikedSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LikedSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        items = Movie.objects.order_by('pk')
        serializer = MovieSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        item = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = MovieSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        items = Music.objects.order_by('pk')
        serializer = MusicSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, pk):
    try:
        item = Music.objects.get(pk=pk)
    except Music.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = MusicSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MusicSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def notificationsettings_list(request):
    if request.method == 'GET':
        items = NotificationSettings.objects.order_by('pk')
        serializer = NotificationSettingsSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NotificationSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def notificationsettings_detail(request, pk):
    try:
        item = NotificationSettings.objects.get(pk=pk)
    except NotificationSettings.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = NotificationSettingsSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NotificationSettingsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def packagesettings_list(request):
    if request.method == 'GET':
        items = PackageSettings.objects.order_by('pk')
        serializer = PackageSettingsSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PackageSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def packagesettings_detail(request, pk):
    try:
        item = PackageSettings.objects.get(pk=pk)
    except PackageSettings.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PackageSettingsSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PackageSettingsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def paymentmethod_list(request):
    if request.method == 'GET':
        items = PaymentMethod.objects.order_by('pk')
        serializer = PaymentMethodSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def paymentmethod_detail(request, pk):
    try:
        item = PaymentMethod.objects.get(pk=pk)
    except PaymentMethod.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PaymentMethodSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PaymentMethodSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def recentlyview_list(request):
    if request.method == 'GET':
        items = RecentlyView.objects.order_by('pk')
        serializer = RecentlyViewSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecentlyViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def recentlyview_detail(request, pk):
    try:
        item = RecentlyView.objects.get(pk=pk)
    except RecentlyView.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = RecentlyViewSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RecentlyViewSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def settingsflag_list(request):
    if request.method == 'GET':
        items = SettingsFlag.objects.order_by('pk')
        serializer = SettingsFlagSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SettingsFlagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def settingsflag_detail(request, pk):
    try:
        item = SettingsFlag.objects.get(pk=pk)
    except SettingsFlag.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = SettingsFlagSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SettingsFlagSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        items = User.objects.order_by('pk')
        serializer = UserSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        item = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def userpayment_list(request):
    if request.method == 'GET':
        items = UserPayment.objects.order_by('pk')
        serializer = UserPaymentSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserPaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def userpayment_detail(request, pk):
    try:
        item = UserPayment.objects.get(pk=pk)
    except UserPayment.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = UserPaymentSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserPaymentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def userplaylist_list(request):
    if request.method == 'GET':
        items = UserPlaylist.objects.order_by('pk')
        serializer = UserPlaylistSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserPlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def userplaylist_detail(request, pk):
    try:
        item = UserPlaylist.objects.get(pk=pk)
    except UserPlaylist.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = UserPlaylistSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserPlaylistSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def userplaylistmusic_list(request):
    if request.method == 'GET':
        items = UserPlaylistMusic.objects.order_by('pk')
        serializer = UserPlaylistMusicSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserPlaylistMusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def userplaylistmusic_detail(request, pk):
    try:
        item = UserPlaylistMusic.objects.get(pk=pk)
    except UserPlaylistMusic.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = UserPlaylistMusicSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserPlaylistMusicSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
