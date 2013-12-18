from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
  # list string -> import ast; ast.literal_eval(actors)
  main = models.ManyToManyField('Character') 
  sub = models.ManyToManyField('SubCharacter') 
  directors = models.ManyToManyField('Director')

  detail_url = models.CharField(max_length=50, null=True, blank=True)
  poster_url = models.CharField(max_length=50, null=True, blank=True)

  title1 = models.CharField(max_length=50, null=True, blank=True)
  title2 = models.CharField(max_length=50, null=True, blank=True)
  story1 = models.CharField(max_length=50, null=True, blank=True)
  story2 = models.TextField()

  country = models.CharField(max_length=20, null=True, blank=True)
  country_code = models.CharField(max_length=5, null=True, blank=True)

  time = models.CharField(max_length=10) # runtime
  year = models.CharField(max_length=10, null=True, blank=True)

  genre = models.CharField(max_length=20, null=True, blank=True)
  open = models.CharField(max_length=15, null=True, blank=True) # date of opened

  form = models.CharField(max_length=10, null=True, blank=True)
  grade = models.CharField(max_length=10, null=True, blank=True)

  code = models.IntegerField(null=True, blank=True)

  rank = models.IntegerField(null=False, default = 0)
  previous_rank = models.IntegerField(null=False, default = 0)

  def __unicode__(self):
    return u"%s" % self.title1

  def genre_as_list(self):
    if self.genre != "":
      return self.genre.split(', ')
    else:
      return False
  def title2_with_link(self):
    if self.title2.find(self.year) != -1 and len(self.title2) - 4 == self.title2.find(self.year):
      return self.title2.replace(self.year, '<a href="/search/movie/year?query='+self.year+'">'+self.year+'</a>')
    else:
      return False

class Actor(models.Model):
  profile_url = models.CharField(max_length=50, null=True, blank=True)
  thumb_url = models.CharField(max_length=50, null=True, blank=True)
  name = models.CharField(max_length=20, null=True, blank=True)
  en_name = models.CharField(max_length=20, null=True, blank=True)
  #part = models.CharField(max_length=20)
  #character = models.CharField(max_length=20)

  #movie_url = models.CharField(max_lenght=50, null=True)

  career1_title = models.CharField(max_length=20, null=True, blank=True)
  career1_year = models.CharField(max_length=10, null=True, blank=True)
  career2_title = models.CharField(max_length=20, null=True, blank=True)
  career2_year= models.CharField(max_length=10, null=True, blank=True)

  code = models.IntegerField(null=True, blank=True)

  rank = models.IntegerField(null=False, default = 0)
  created_on = models.DateTimeField(auto_now_add=True, auto_now=True)
  previous_rank = models.IntegerField(null=False, default = 0)

  def __unicode__(self):
    return u"%s" % self.name

class Character(models.Model):
  actor = models.ForeignKey(Actor)

  part = models.CharField(max_length=20, null=True, blank=True)
  character = models.CharField(max_length=20, null=True, blank=True)

  def __unicode__(self):
    return u"%s (%s)" %(self.character, self.actor.name)

class SubCharacter(models.Model):
  actor = models.ForeignKey(Actor)

  #profile_url = models.CharField(max_length=50)
  #name = models.CharField(max_length=20)
  character = models.CharField(max_length=20, null=True, blank=True)

  def __unicode__(self):
    return u"%s (%s)" %(self.character, self.actor.name)

class Director(models.Model):
  profile_url = models.CharField(max_length=50, null=True, blank=True)
  thumb_url = models.CharField(max_length=50, null=True, blank=True)
  name = models.CharField(max_length=20, null=True, blank=True)
  en_name = models.CharField(max_length=20, null=True, blank=True)
  code = models.IntegerField(null=True, blank=True)

  def __unicode__(self):
    return u"%s" % self.name

class Movie_List(models.Model):
  name = models.CharField(max_length=30)
  description = models.CharField(max_length=300)

  like = models.IntegerField()
  dislike = models.IntegerField()

  movie = models.ManyToManyField(Movie)

  #creator = models.ForeignKey('account.models.UserProfile')
  created_date = models.DateField()

  def __unicode__(self):
    return u"%s" % self.name
