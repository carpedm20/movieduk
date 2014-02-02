sqlite3 movieduk.sqlite
drop south_migrationhistory;
drop table account_dukuser;
...
drop table userinfo_liked_list;
...

rm -rf account/migrations
python manage.py schemamigration account --init
python manage.py schemamigration account --auto
python manage.py migrate account --delete-ghost-migrations

from account.models import *
DukUser.objects.all()
DukUser.objects.all()[0].delete()

drop table UserInfo_userinfo;
drop table UserInfo_userinfo_actor_disliked;
drop table UserInfo_userinfo_actor_liked;
drop table UserInfo_userinfo_director_disliked;
drop table UserInfo_userinfo_director_liked;
drop table UserInfo_userinfo_disliked;
drop table UserInfo_userinfo_disliked_list;
drop table UserInfo_userinfo_liked;
drop table UserInfo_userinfo_liked_list;
drop table UserInfo_userinfo_own_list;
drop table UserInfo_userinfo_watched;
drop table UserInfo_userinfo_watchlist;
drop table UserMovie_userinfo;
drop table UserMovie_userinfo_actor_disliked;
drop table UserMovie_userinfo_actor_liked;
drop table UserMovie_userinfo_director_disliked;
drop table UserMovie_userinfo_director_liked;
drop table UserMovie_userinfo_disliked;
drop table UserMovie_userinfo_disliked_list;
drop table UserMovie_userinfo_liked;
drop table UserMovie_userinfo_liked_list;
drop table UserMovie_userinfo_own_list;
drop table UserMovie_userinfo_watched;
drop table UserMovie_userinfo_watchlist;

######################
# django-social-auth #
######################

# dict, .json, not callable blabla error
sudo pip install requests --upgrade

##################
# make sql query #
##################

# python manage.py sqlall account

#########
# south #
#########

# no such column
python manage.py schemamigration account --add-field DukUser.is_active
python manage.py schemamigration core --add-model File
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


