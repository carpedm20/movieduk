# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Award'
        db.create_table(u'core_award', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('prize', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('rnd', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Award'])

        # Adding M2M table for field movie on 'Award'
        m2m_table_name = db.shorten_name(u'core_award_movie')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('award', models.ForeignKey(orm[u'core.award'], null=False)),
            ('movie', models.ForeignKey(orm[u'core.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['award_id', 'movie_id'])

        # Adding model 'MovieList'
        db.create_table(u'core_movielist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['MovieList'])

        # Adding M2M table for field movies on 'MovieList'
        m2m_table_name = db.shorten_name(u'core_movielist_movies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movielist', models.ForeignKey(orm[u'core.movielist'], null=False)),
            ('movie', models.ForeignKey(orm[u'core.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movielist_id', 'movie_id'])

        # Adding field 'Actor.birth'
        db.add_column(u'core_actor', 'birth',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Actor.country'
        db.add_column(u'core_actor', 'country',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Actor.detail'
        db.add_column(u'core_actor', 'detail',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding M2M table for field awards on 'Actor'
        m2m_table_name = db.shorten_name(u'core_actor_awards')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actor', models.ForeignKey(orm[u'core.actor'], null=False)),
            ('award', models.ForeignKey(orm[u'core.award'], null=False))
        ))
        db.create_unique(m2m_table_name, ['actor_id', 'award_id'])


    def backwards(self, orm):
        # Deleting model 'Award'
        db.delete_table(u'core_award')

        # Removing M2M table for field movie on 'Award'
        db.delete_table(db.shorten_name(u'core_award_movie'))

        # Deleting model 'MovieList'
        db.delete_table(u'core_movielist')

        # Removing M2M table for field movies on 'MovieList'
        db.delete_table(db.shorten_name(u'core_movielist_movies'))

        # Deleting field 'Actor.birth'
        db.delete_column(u'core_actor', 'birth')

        # Deleting field 'Actor.country'
        db.delete_column(u'core_actor', 'country')

        # Deleting field 'Actor.detail'
        db.delete_column(u'core_actor', 'detail')

        # Removing M2M table for field awards on 'Actor'
        db.delete_table(db.shorten_name(u'core_actor_awards'))


    models = {
        u'core.actor': {
            'Meta': {'object_name': 'Actor'},
            'awards': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Award']", 'symmetrical': 'False'}),
            'birth': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'career1_title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'career1_year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'career2_title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'career2_year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'detail': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'en_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'previous_rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'profile_url': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thumb_url': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'core.award': {
            'Meta': {'object_name': 'Award'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Movie']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'prize': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'rnd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'core.character': {
            'Meta': {'object_name': 'Character'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Actor']"}),
            'character': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'core.director': {
            'Meta': {'object_name': 'Director'},
            'code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'en_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'profile_url': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'thumb_url': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'core.movie': {
            'Meta': {'object_name': 'Movie'},
            'code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'detail_url': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'directors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Director']", 'symmetrical': 'False'}),
            'form': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Character']", 'symmetrical': 'False'}),
            'open': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'poster_url': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'previous_rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'story1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'story2': ('django.db.models.fields.TextField', [], {}),
            'sub': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.SubCharacter']", 'symmetrical': 'False'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'title1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'title2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'core.movie_list': {
            'Meta': {'object_name': 'Movie_List'},
            'created_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'dislike': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {}),
            'movie': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Movie']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'core.movielist': {
            'Meta': {'object_name': 'MovieList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Movie']", 'symmetrical': 'False'})
        },
        u'core.subcharacter': {
            'Meta': {'object_name': 'SubCharacter'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Actor']"}),
            'character': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']