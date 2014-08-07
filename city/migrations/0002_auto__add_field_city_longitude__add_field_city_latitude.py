# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'City.longitude'
        db.add_column(u'city_city', 'longitude',
                      self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=10),
                      keep_default=False)

        # Adding field 'City.latitude'
        db.add_column(u'city_city', 'latitude',
                      self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=15, decimal_places=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'City.longitude'
        db.delete_column(u'city_city', 'longitude')

        # Deleting field 'City.latitude'
        db.delete_column(u'city_city', 'latitude')


    models = {
        u'city.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '10'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['city']