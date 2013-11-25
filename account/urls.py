from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  url(r'^profile/$','account.views.view_profile'),
)
