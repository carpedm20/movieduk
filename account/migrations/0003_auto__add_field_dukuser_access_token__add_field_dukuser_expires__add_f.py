# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DukUser.access_token'
        db.add_column(u'account_dukuser', 'access_token',
                      self.gf('django.db.models.fields.CharField')(max_length=103, unique=True, null=True),
                      keep_default=False)

        # Adding field 'DukUser.expires'
        db.add_column(u'account_dukuser', 'expires',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'DukUser.uid'
        db.add_column(u'account_dukuser', 'uid',
                      self.gf('django.db.models.fields.BigIntegerField')(unique=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DukUser.access_token'
        db.delete_column(u'account_dukuser', 'access_token')

        # Deleting field 'DukUser.expires'
        db.delete_column(u'account_dukuser', 'expires')

        # Deleting field 'DukUser.uid'
        db.delete_column(u'account_dukuser', 'uid')


    models = {
        u'account.dukuser': {
            'Meta': {'object_name': 'DukUser'},
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