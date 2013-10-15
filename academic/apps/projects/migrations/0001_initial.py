# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Topic'
        db.create_table(u'projects_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('highlight', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('highlight_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=2048, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=128)),
            ('excerpt', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'projects', ['Topic'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('highlight', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('redirect_to', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('short_title', self.gf('django.db.models.fields.CharField')(max_length=1024, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=128)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=2048, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('excerpt', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('footer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects', to=orm['projects.Topic'])),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding M2M table for field downloads on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_downloads')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('download', models.ForeignKey(orm[u'content.download'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'download_id'])

        # Adding M2M table for field people on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_people')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('person', models.ForeignKey(orm[u'people.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'person_id'])

        # Adding M2M table for field organizations on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_organizations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('organization', models.ForeignKey(orm[u'organizations.organization'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'organization_id'])

        # Adding M2M table for field publications on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_publications')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('publication', models.ForeignKey(orm[u'publishing.publication'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'publication_id'])

        # Adding M2M table for field sponsors on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_sponsors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('sponsor', models.ForeignKey(orm[u'organizations.sponsor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'sponsor_id'])

        # Adding M2M table for field related_topics on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_related_topics')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('topic', models.ForeignKey(orm[u'projects.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'topic_id'])


    def backwards(self, orm):
        # Deleting model 'Topic'
        db.delete_table(u'projects_topic')

        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Removing M2M table for field downloads on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_downloads'))

        # Removing M2M table for field people on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_people'))

        # Removing M2M table for field organizations on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_organizations'))

        # Removing M2M table for field publications on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_publications'))

        # Removing M2M table for field sponsors on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_sponsors'))

        # Removing M2M table for field related_topics on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_related_topics'))


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
        u'projects.project': {
            'Meta': {'ordering': "['topic', 'modified', 'created']", 'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'downloads': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['content.Download']", 'null': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'footer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'highlight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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