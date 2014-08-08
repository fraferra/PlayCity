# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shop'
        db.create_table(u'shop_shop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(default='Super shop!', max_length=100, null=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('picture_url', self.gf('django.db.models.fields.CharField')(default='/static/img/stanford.png', max_length=200, null=True)),
        ))
        db.send_create_signal(u'shop', ['Shop'])

        # Adding model 'Coupon'
        db.create_table(u'shop_coupon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500, null=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=0)),
            ('picture_url', self.gf('django.db.models.fields.CharField')(default='/static/img/stanford.png', max_length=200, null=True)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Shop'])),
            ('coupons_released', self.gf('django.db.models.fields.DecimalField')(default=10, max_digits=4, decimal_places=0)),
        ))
        db.send_create_signal(u'shop', ['Coupon'])

        # Adding M2M table for field buyers on 'Coupon'
        m2m_table_name = db.shorten_name(u'shop_coupon_buyers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coupon', models.ForeignKey(orm[u'shop.coupon'], null=False)),
            ('player', models.ForeignKey(orm[u'play.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coupon_id', 'player_id'])


    def backwards(self, orm):
        # Deleting model 'Shop'
        db.delete_table(u'shop_shop')

        # Deleting model 'Coupon'
        db.delete_table(u'shop_coupon')

        # Removing M2M table for field buyers on 'Coupon'
        db.delete_table(db.shorten_name(u'shop_coupon_buyers'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'city.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '10'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '15', 'decimal_places': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'play.player': {
            'Meta': {'object_name': 'Player'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'city'", 'null': 'True', 'to': u"orm['city.City']"}),
            'experience': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '5', 'decimal_places': '0'}),
            'facebook_pic': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '4', 'decimal_places': '0'}),
            'picture_url': ('django.db.models.fields.CharField', [], {'default': "'/static/img/avatar-1.png'", 'max_length': '400', 'null': 'True'}),
            'score': ('django.db.models.fields.DecimalField', [], {'default': '20', 'null': 'True', 'max_digits': '4', 'decimal_places': '0'}),
            'token': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'shop.coupon': {
            'Meta': {'object_name': 'Coupon'},
            'buyers': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': u"orm['play.Player']", 'null': 'True', 'symmetrical': 'False'}),
            'coupons_released': ('django.db.models.fields.DecimalField', [], {'default': '10', 'max_digits': '4', 'decimal_places': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'picture_url': ('django.db.models.fields.CharField', [], {'default': "'/static/img/stanford.png'", 'max_length': '200', 'null': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '0'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Shop']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        u'shop.shop': {
            'Meta': {'object_name': 'Shop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'picture_url': ('django.db.models.fields.CharField', [], {'default': "'/static/img/stanford.png'", 'max_length': '200', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Super shop!'", 'max_length': '100', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['shop']