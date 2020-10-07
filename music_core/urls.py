from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from music_core import views


urlpatterns = [

    url(r'^admin/(?P<pk>[0-9]+)/$', views.admin_detail),
    url(r'^admin/$', views.admin_list),

    url(r'^adssettings/(?P<pk>[0-9]+)/$', views.adssettings_detail),
    url(r'^adssettings/$', views.adssettings_list),

    url(r'^album/(?P<pk>[0-9]+)/$', views.album_detail),
    url(r'^album/$', views.album_list),

    url(r'^apilist/(?P<pk>[0-9]+)/$', views.apilist_detail),
    url(r'^apilist/$', views.apilist_list),

    url(r'^apilistparameters/(?P<pk>[0-9]+)/$', views.apilistparameters_detail),
    url(r'^apilistparameters/$', views.apilistparameters_list),

    url(r'^artist/(?P<pk>[0-9]+)/$', views.artist_detail),
    url(r'^artist/$', views.artist_list),

    url(r'^bannerslider/(?P<pk>[0-9]+)/$', views.bannerslider_detail),
    url(r'^bannerslider/$', views.bannerslider_list),

    url(r'^category/(?P<pk>[0-9]+)/$', views.category_detail),
    url(r'^category/$', views.category_list),

    url(r'^homecomponents/(?P<pk>[0-9]+)/$', views.homecomponents_detail),
    url(r'^homecomponents/$', views.homecomponents_list),

    url(r'^liked/(?P<pk>[0-9]+)/$', views.liked_detail),
    url(r'^liked/$', views.liked_list),

    url(r'^movie/(?P<pk>[0-9]+)/$', views.movie_detail),
    url(r'^movie/$', views.movie_list),

    url(r'^music/(?P<pk>[0-9]+)/$', views.music_detail),
    url(r'^music/$', views.music_list),

    url(r'^notificationsettings/(?P<pk>[0-9]+)/$', views.notificationsettings_detail),
    url(r'^notificationsettings/$', views.notificationsettings_list),

    url(r'^packagesettings/(?P<pk>[0-9]+)/$', views.packagesettings_detail),
    url(r'^packagesettings/$', views.packagesettings_list),

    url(r'^paymentmethod/(?P<pk>[0-9]+)/$', views.paymentmethod_detail),
    url(r'^paymentmethod/$', views.paymentmethod_list),

    url(r'^recentlyview/(?P<pk>[0-9]+)/$', views.recentlyview_detail),
    url(r'^recentlyview/$', views.recentlyview_list),

    url(r'^settingsflag/(?P<pk>[0-9]+)/$', views.settingsflag_detail),
    url(r'^settingsflag/$', views.settingsflag_list),

    url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^user/$', views.user_list),

    url(r'^userpayment/(?P<pk>[0-9]+)/$', views.userpayment_detail),
    url(r'^userpayment/$', views.userpayment_list),

    url(r'^userplaylist/(?P<pk>[0-9]+)/$', views.userplaylist_detail),
    url(r'^userplaylist/$', views.userplaylist_list),

    url(r'^userplaylistmusic/(?P<pk>[0-9]+)/$', views.userplaylistmusic_detail),
    url(r'^userplaylistmusic/$', views.userplaylistmusic_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
