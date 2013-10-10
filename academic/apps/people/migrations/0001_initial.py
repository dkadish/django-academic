# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rank'
        db.create_table(u'people_rank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('plural_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'people', ['Rank'])

        # Adding model 'Person'
        db.create_table(u'people_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('visitor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('alumni', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('rank', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='people', null=True, to=orm['people.Rank'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('mid_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('e_mail', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('web_page', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(default='people/default.jpg', max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'people', ['Person'])

        # Adding unique constraint on 'Person', fields ['first_name', 'mid_name', 'last_name']
        db.create_unique(u'people_person', ['first_name', 'mid_name', 'last_name'])

        # Adding M2M table for field affiliation on 'Person'
        m2m_table_name = db.shorten_name(u'people_person_affiliation')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'people.person'], null=False)),
            ('organization', models.ForeignKey(orm[u'organizations.organization'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'organization_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Person', fields ['first_name', 'mid_name', 'last_name']
        db.delete_unique(u'people_person', ['first_name', 'mid_name', 'last_name'])

        # Deleting model 'Rank'
        db.delete_table(u'people_rank')

        # Deleting model 'Person'
        db.delete_table(u'people_person')

        # Removing M2M table for field affiliation on 'Person'
        db.delete_table(db.shorten_name(u'people_person_affiliation'))


    models = {
        u'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'db_index': 'True', 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_index': 'True'}),
            'web_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'people.person': {
            'Meta': {'ordering': "['rank', 'last_name', 'first_name']", 'unique_together': "(('first_name', 'mid_name', 'last_name'),)", 'object_name': 'Person'},
            'affiliation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'people'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['organizations.Organization']"}),
            'alumni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'e_mail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'mid_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': "'people/default.jpg'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rank': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'people'", 'null': 'True', 'to': u"orm['people.Rank']"}),
            'visitor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'web_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'people.rank': {
            'Meta': {'ordering': "['order']", 'object_name': 'Rank'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'plural_name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['people']