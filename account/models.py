from django.db import models
from core.models import *

class CustomUserManager(models.Manager):
  def create_user(self, username, email=None):
    return self.model._default_manager.create(username=username)

class DukUser(models.Model):
  #social_auth requirements
  username = models.CharField(max_length=30)
  email = models.EmailField(blank=True, null=True)
  last_login = models.DateTimeField(blank=True, null=True)
  is_active = models.BooleanField(default=True)

  friends = models.ManyToManyField('self', blank = True, null = True)

  gender = models.CharField(max_length=10, blank=True)
  locale = models.CharField(max_length=10, blank=True)

  objects = CustomUserManager()

  own_movielist = models.ManyToManyField(MovieList, related_name = 'own_movielist')
  liked_movielist = models.ManyToManyField(MovieList, related_name = 'liked_movielist')
  hated_movielist = models.ManyToManyField(MovieList, related_name = 'hated_movielist')

  watched_movie = models.ManyToManyField(Movie, related_name = 'watched_movie')
  liked_movie = models.ManyToManyField(Movie, related_name = 'liked_movie')
  hated_movie = models.ManyToManyField(Movie, related_name = 'hated_movie')
  watchlist_movie  = models.ManyToManyField(Movie, related_name = 'watchlist_movie')

  followed_tag = models.ManyToManyField(Tag, blank=True, null = True)

  def __unicode__(self):
    return self.username

  def is_authenticated(self):
    return True

  def facebook_extra_values(sender, user,response, details, **kwargs):     
    profile = user.get_profile()
    current_user = user 
    profile, new = UserProfile.objects.get_or_create(user=current_user)

    profile.gender = response.get('gender')
    profile.locale = response.get('locale')
    profile.save()
    return True
