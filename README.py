######################
# django-social-auth #
######################

# dict, .json, not callable blabla error
sudo pip install requests --upgrade

#########
# south #
#########

# no such column
python manage.py schemamigration account --add-field DukUser.is_active
python manage.py migrate account

"""
rm account/migrations/*
python manage.py syncdb
python manage.py schemamigration account --initial
python manage.py migrate account  --delete-ghost-migrations
"""

##########
# export #
##########

from django.core import serializers
from core.models import *
data = serializers.serialize("json", Movie.objects.all())
out = open("core.movie.json", "w")
out.write(data)
out.close()

data = serializers.serialize("json", Actor.objects.all())
out = open("core.actor.json", "w")
out.write(data)
out.close()

data = serializers.serialize("json", Character.objects.all())
out = open("core.character.json", "w")
out.write(data)
out.close()

data = serializers.serialize("json", SubCharacter.objects.all())
out = open("core.subCharacter.json", "w")
out.write(data)
out.close()

data = serializers.serialize("json", Director.objects.all())
out = open("core.director.json", "w")
out.write(data)
out.close()


