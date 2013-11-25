from django.conf.urls import patterns, *
from core.models import Movie 

urlpatterns = patterns('core.views',
    #url(r'^new/$', 'new_movie', name='new_movie'),
    #url(r'movie/add/$', generic.CreateView.as_view(
    #    model=Movie, form_class=MovieForm)),
    #url(r'movie/(?P<pk>\d+)/update/$', generic.UpdateView.as_view(
    #    model=Widget, form_class=WidgetForm), name='widget_update'),
)
