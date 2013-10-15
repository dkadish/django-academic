# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Involvement.role'
        db.add_column(u'projects_involvement', 'role',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['projects.Role']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Involvement.role'
        db.delete_column(u'projects_involvement', 'role_id')


    models = {
        u'content.download': {
            'Meta': {'ordering': "['title']", 'object_name': 'Download'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'db_index': 'True', 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_index': 'True'}),
            'web_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'organizations.sponsor': {
            'Meta': {'ordering': "['order', 'name']", 'object_name': 'Sponsor', '_ormbases': [u'organizations.Organization']},
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            u'organization_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['organizations.Organization']", 'unique': 'True', 'primary_key': 'True'})
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
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': "'/home/dkadish/workspace/cct.ok.ubc.ca/src/academic/people/default.jpg'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rank': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'people'", 'null': 'True', 'to': u"orm['people.Rank']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'visitor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'web_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'people.rank': {
            'Meta': {'ordering': "['order']", 'object_name': 'Rank'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'plural_name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'projects.involvement': {
            'Meta': {'object_name': 'Involvement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Role']"})
        },
        u'projects.project': {
            'Meta': {'ordering': "['topic', 'modified', 'created']", 'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'downloads': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['content.Download']", 'null': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'footer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'highlight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'organizations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'projects'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['organizations.Organization']"}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': u"orm['people.Person']"}),
            'publications': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['publishing.Publication']", 'null': 'True', 'blank': 'True'}),
            'redirect_to': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'related_topics': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'secondary_projects'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['projects.Topic']"}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'sponsors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['organizations.Sponsor']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'db_index': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': u"orm['projects.Topic']"})
        },
        u'projects.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'plural_name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'projects.topic': {
            'Meta': {'ordering': "['title']", 'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'excerpt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'highlight': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'highlight_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'db_index': 'True'})
        },
        u'publishing.authorship': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Authorship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishing.Publication']"})
        },
        u'publishing.publication': {
            'Meta': {'ordering': "['-year', '-month']", 'unique_together': "(('title', 'year'),)", 'object_name': 'Publication'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'publications'", 'to': u"orm['people.Person']", 'through': u"orm['publishing.Authorship']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'bibtex': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'fulltext': ('django.db.models.fields.files.FileField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '512'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'db_index': 'True'})
        }
    }

    complete_apps = ['projects']