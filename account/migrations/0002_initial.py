# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DukUser'
        db.create_table(u'account_dukuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=254)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('synergy_level', self.gf('django.db.models.fields.IntegerField')()),
            ('is_team_player', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'account', ['DukUser'])


    def backwards(self, orm):
        # Deleting model 'DukUser'
        db.delete_table(u'account_dukuser')


    models = {
        u'account.dukuser': {
            'Meta': {'object_name': 'DukUser'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_team_player': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'synergy_level': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '254'})
        }
    }

    complete_apps = ['account']