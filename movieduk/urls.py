from django.conf.urls import patterns, include, url

#import autocomplete_light
#autocomplete_light.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from movieduk import settings

urlpatterns = patterns('',
    (r'^account/', include('account.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    (r'^asset/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.ASSET_ROOT}),
    url(r'^api/get_info/', 'core.views.get_info', name='get_info'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.index'),
    url(r'^index$', 'core.views.index'),
    url(r'^search/movie/(?P<option>\w+)', 'core.views.movie_search', name='movie_search'),
    url(r'^info/director/(?P<code>\d+)', 'core.views.director_info'),
    url(r'^info/actor/(?P<code>\d+)', 'core.views.actor_info'),
    url(r'^info/movie/(?P<code>\d+)', 'core.views.movie_info'),
    url(r'^login', 'account.views.sign_in'),
    url(r'^logout', 'account.views.sign_out'),
    url(r'^join', 'account.views.sign_up', name='login'),
    url(r'^search/profile/', 'core.views.movie_search', name='movie_search'),
    #url(r'autocomplete/', include('autocomplete_light.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
