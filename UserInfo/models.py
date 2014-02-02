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

  actor_liked = models.ManyToManyField(Actor, blank=True, null=True, related_name = 'actor_liked')
  actor_disliked = models.ManyToManyField(Actor, blank=True, null=True, related_name = 'actor_disliked')
  director_liked = models.ManyToManyField(Director, blank=True, null=True, related_name = 'director_liked')
  director_disliked = models.ManyToManyField(Director, blank=True, null=True, related_name = 'director_disliked')

  def __unicode__(self):
    return self.username
