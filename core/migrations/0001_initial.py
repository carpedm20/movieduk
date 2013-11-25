# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'core_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('detail_url', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('poster_url', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('title1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('title2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('story1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('story2', self.gf('django.db.models.fields.TextField')()),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('open', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('form', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Movie'])

        # Adding M2M table for field main on 'Movie'
        m2m_table_name = db.shorten_name(u'core_movie_main')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'core.movie'], null=False)),
            ('character', models.ForeignKey(orm[u'core.character'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'character_id'])

        # Adding M2M table for field sub on 'Movie'
        m2m_table_name = db.shorten_name(u'core_movie_sub')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'core.movie'], null=False)),
            ('subcharacter', models.ForeignKey(orm[u'core.subcharacter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'subcharacter_id'])

        # Adding M2M table for field directors on 'Movie'
        m2m_table_name = db.shorten_name(u'core_movie_directors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'core.movie'], null=False)),
            ('director', models.ForeignKey(orm[u'core.director'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'director_id'])

        # Adding model 'Actor'
        db.create_table(u'core_actor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile_url', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('thumb_url', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('en_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('career1_title', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('career1_year', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('career2_title', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('career2_year', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Actor'])

        # Adding model 'Character'
        db.create_table(u'core_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Actor'])),
            ('part', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('character', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Character'])

        # Adding model 'SubCharacter'
        db.create_table(u'core_subcharacter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Actor'])),
            ('character', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['SubCharacter'])

        # Adding model 'Director'
        db.create_table(u'core_director', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile_url', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('thumb_url', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('en_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Director'])

        # Adding model 'Movie_List'
        db.create_table(u'core_movie_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('like', self.gf('django.db.models.fields.IntegerField')()),
            ('dislike', self.gf('django.db.models.fields.IntegerField')()),
            ('created_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'core', ['Movie_List'])

        # Adding M2M table for field movie on 'Movie_List'
        m2m_table_name = db.shorten_name(u'core_movie_list_movie')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie_list', models.ForeignKey(orm[u'core.movie_list'], null=False)),
            ('movie', models.ForeignKey(orm[u'core.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_list_id', 'movie_id'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'core_movie')

        # Removing M2M table for field main on 'Movie'
        db.delete_table(db.shorten_name(u'core_movie_main'))

        # Removing M2M table for field sub on 'Movie'
        db.delete_table(db.shorten_name(u'core_movie_sub'))

        # Removing M2M table for field directors on 'Movie'
        db.delete_table(db.shorten_name(u'core_movie_directors'))

        # Deleting model 'Actor'
        db.delete_table(u'core_actor')

        # Deleting model 'Character'
        db.delete_table(u'core_character')

        # Deleting model 'SubCharacter'
        db.delete_table(u'core_subcharacter')

        # Deleting model 'Director'
        db.delete_table(u'core_director')

        # Deleting model 'Movie_List'
        db.delete_table(u'core_movie_list')

        # Removing M2M table for field movie on 'Movie_List'
        db.delete_table(db.shorten_name(u'core_movie_list_movie'))


    models = {
        u'core.actor': {
            'Meta': {'object_name': 'Actor'},
            'career1_title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'career1_year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'career2_title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'career2_year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'en_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'profile_url': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'thumb_url': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
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
        u'core.subcharacter': {
            'Meta': {'object_name': 'SubCharacter'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Actor']"}),
            'character': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']