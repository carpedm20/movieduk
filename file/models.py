from django.db import models
from core.models import Movie
# Create your models here.

class File(models.Model):
  movie = models.ManyToManyField(Movie)

  #file_name = models.CharField(max_length=50, default='')
  #directory = models.CharField(max_length=50, default='')
  file_field = models.FileField(default = None, blank=True, upload_to='video')
  subtitle_name = models.CharField(max_length=50, default='')

  uploaded_date = models.DateField(auto_now_add = True, null=True)

  view_count = models.IntegerField(default = 0, null = False)
  download_count = models.IntegerField(default = 0, null = False)

  is_drama = models.BooleanField(default=False)

  season = models.IntegerField(default = -1)
  episode = models.IntegerField(default = -1)

  def __unicode__(self):
    return self.directory + '/' + self.file_name

  def get_full_path(self):
    return 'video/' + self.directory + '/' + self.file_name

