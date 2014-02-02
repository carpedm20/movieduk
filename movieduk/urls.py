from django.conf.urls import patterns, include, url

#import autocomplete_light
#autocomplete_light.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from movieduk import settings

urlpatterns = patterns('',
    #(r'^account/', include('account.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    (r'^asset/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.ASSET_ROOT}),
    url(r'^api/get_info/', 'core.views.get_info', name='get_info'),
    url(r'^api/get_search_list/', 'core.views.get_search_list', name='get_search_list'),
    url(r'^api/get_list/', 'core.views.get_list', name='get_list'),
    url(r'^api/get_short_list/', 'core.views.get_short_list', name='get_short_list'),

    url(r'^rank', 'rank.views.index', name='index'),
    url(r'^api/get_rank/', 'rank.views.get_rank', name='get_rank'),

    url(r'^api/is_login', 'account.views.is_login', name='is_login'),
    url(r'^api/check_movie', 'account.views.check_movie', name='check_movie'),
    url(r'^profile', 'account.views.profile', name='profile'),
    url(r'^social', 'account.views.social', name='social'),

    #url(r'', include('social_auth.urls')),
    url(r'^login', 'account.views.sign_in'),
    url(r'^logout', 'account.views.sign_out'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'core.views.index'),
    url(r'^short', 'core.views.index_short'),
    url(r'^index$', 'core.views.index'),
    url(r'^random', 'core.views.random', name='index'),

    url(r'^search/movie/(?P<option>\w+)', 'core.views.movie_search', name='movie_search'),
    url(r'^filter', 'core.views.movie_filter'),
    url(r'^filter/short', 'core.views.movie_filter'),
    url(r'^info/director/(?P<code>\d+)', 'core.views.director_info'),
    url(r'^info/actor/(?P<code>\d+)', 'core.views.actor_info'),
    url(r'^info/movie/(?P<code>\d+)', 'core.views.movie_info'),

    #url(r'autocomplete/', include('autocomplete_light.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
