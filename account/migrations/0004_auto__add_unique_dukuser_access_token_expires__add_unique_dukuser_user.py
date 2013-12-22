# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'DukUser', fields ['access_token', 'expires']
        db.create_unique(u'account_dukuser', ['access_token', 'expires'])

        # Adding unique constraint on 'DukUser', fields ['username', 'uid']
        db.create_unique(u'account_dukuser', ['username', 'uid'])


    def backwards(self, orm):
        # Removing unique constraint on 'DukUser', fields ['username', 'uid']
        db.delete_unique(u'account_dukuser', ['username', 'uid'])

        # Removing unique constraint on 'DukUser', fields ['access_token', 'expires']
        db.delete_unique(u'account_dukuser', ['access_token', 'expires'])


    models = {
        u'account.dukuser': {
            'Meta': {'unique_together': "(('username', 'uid'), ('access_token', 'expires'))", 'object_name': 'DukUser'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '103', 'unique': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'expires': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['account']