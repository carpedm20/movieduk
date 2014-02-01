from django.db import models
from core.models import *

class MovieUser(models.Model):
  print "==============DUKUSERCREATE"
  #social_auth requirements
  username = models.CharField(max_length=30)
  first_name = models.CharField(max_length=10, blank=True, null=True)
  last_name = models.CharField(max_length=10, blank=True, null=True)
  password = models.CharField(max_length=30)

  email = models.EmailField(blank=True, null=True)
  last_login = models.DateTimeField(blank=True, null=True)
  is_active = models.BooleanField(default=True)

  friends = models.ManyToManyField('self', blank = True, null = True, related_name='friends', through='followed_friends', symmetrical=False)

  gender = models.CharField(max_length=10, blank=True)
  locale = models.CharField(max_length=10, blank=True)

  own_movielists = models.ManyToManyField(MovieList, blank=True, null=True, related_name = 'own_movielists')
  liked_movielist = models.ManyToManyField(MovieList, blank=True, null=True, related_name = 'liked_movielist')
  hated_movielist = models.ManyToManyField(MovieList, blank=True, null=True, related_name = 'hated_movielist')

  watched_movie = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'watched_movie')
  liked_movie = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'liked_movie')
  hated_movie = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'hated_movie')
  watchlist_movie  = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'watchlist_movie')

  def __unicode__(self):
    return self.username
