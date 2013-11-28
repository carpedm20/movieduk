# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FacebookSession'
        db.create_table(u'facebook_account_facebooksession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('access_token', self.gf('django.db.models.fields.CharField')(unique=True, max_length=103)),
            ('expires', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.DukUser'], null=True)),
            ('uid', self.gf('django.db.models.fields.BigIntegerField')(unique=True, null=True)),
        ))
        db.send_create_signal(u'facebook_account', ['FacebookSession'])

        # Adding unique constraint on 'FacebookSession', fields ['user', 'uid']
        db.create_unique(u'facebook_account_facebooksession', ['user_id', 'uid'])

        # Adding unique constraint on 'FacebookSession', fields ['access_token', 'expires']
        db.create_unique(u'facebook_account_facebooksession', ['access_token', 'expires'])


    def backwards(self, orm):
        # Removing unique constraint on 'FacebookSession', fields ['access_token', 'expires']
        db.delete_unique(u'facebook_account_facebooksession', ['access_token', 'expires'])

        # Removing unique constraint on 'FacebookSession', fields ['user', 'uid']
        db.delete_unique(u'facebook_account_facebooksession', ['user_id', 'uid'])

        # Deleting model 'FacebookSession'
        db.delete_table(u'facebook_account_facebooksession')


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
        },
        u'facebook_account.facebooksession': {
            'Meta': {'unique_together': "(('user', 'uid'), ('access_token', 'expires'))", 'object_name': 'FacebookSession'},
            'access_token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '103'}),
            'expires': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.DukUser']", 'null': 'True'})
        }
    }

    complete_apps = ['facebook_account']