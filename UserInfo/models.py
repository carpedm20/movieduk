from django.db import models
from core.models import *

class UserInfo(models.Model):
  owner = models.ForeignKey(User)

  own_list = models.ManyToManyField(MovieList, blank=True, null=True, related_name = 'own_list')
  liked_list = models.ManyToManyField(MovieList, blank=True, null=True, related_name = 'liked_list')
  disliked_list = models.ManyToManyField(MovieList, blank=True, null=True, related_name = 'disliked_list')

  watched = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'watched')
  liked = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'liked')
  disliked = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'disliked')
  watchlist = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'watchlist')

  def __unicode__(self):
    return self.username
