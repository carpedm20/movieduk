from django import forms

from core.models import Movie

class CoreForm(forms.ModelForm):
  class Meta:
    model = Movie
    fields = ('title1',)

class CoreListForm(forms.Form):
  def __init__(self, *args, **kwargs):
    movies = kwargs.pop('movies', [])
    print "[forms.py] len of movies : " + str(len(movies))
 
    super(CoreListForm, self).__init__(*args, **kwargs)

    count = 0
    for movie in movies:
      if count == 20:
        break
      field = movie.title1.encode('utf-8')
      #self.fields[field] = forms.BooleanField(required = False, label = movie.title)
      self.fields['movies'] = forms.BooleanField(required = False, label = movie.title1)

      count += 1

  def clean(self):
    selected = [tids for tid, val in self.cleaned_data.items() if val]
    if not selected:
      raise forms.ValidationError("You need to select one or more items!")
    return selected

