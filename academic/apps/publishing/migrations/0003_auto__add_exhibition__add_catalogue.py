# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exhibition'
        db.create_table(u'publishing_exhibition', (
            (u'publication_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['publishing.Publication'], unique=True, primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('medium', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('show', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'publishing', ['Exhibition'])

        # Adding model 'Catalogue'
        db.create_table(u'publishing_catalogue', (
            (u'book_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['publishing.Book'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'publishing', ['Catalogue'])


    def backwards(self, orm):
        # Deleting model 'Exhibition'
        db.delete_table(u'publishing_exhibition')

        # Deleting model 'Catalogue'
        db.delete_table(u'publishing_catalogue')


    models = {
        u'organizations.institution': {
            'Meta': {'object_name': 'Institution', '_ormbases': [u'organizations.Organization']},
            u'organization_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['organizations.Organization']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'db_index': 'True', 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_index': 'True'}),
            'web_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'organizations.publisher': {
            'Meta': {'object_name': 'Publisher', '_ormbases': [u'organizations.Organization']},
            u'organization_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['organizations.Organization']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'organizations.school': {
            'Meta': {'object_name': 'School', '_ormbases': [u'organizations.Organization']},
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
            'listed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mid_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': "'academic/people/default.jpg'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
        u'publishing.advisorship': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Advisorship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishing.Thesis']"})
        },
        u'publishing.authorship': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Authorship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishing.Publication']"})
        },
        u'publishing.book': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'Book', '_ormbases': [u'publishing.Publication']},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'editors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'proceedings'", 'to': u"orm['people.Person']", 'through': u"orm['publishing.Editorship']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'publication_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Publication']", 'unique': 'True', 'primary_key': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'books'", 'null': 'True', 'to': u"orm['organizations.Publisher']"}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'publishing.bookchapter': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'BookChapter', '_ormbases': [u'publishing.Book']},
            u'book_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Book']", 'unique': 'True', 'primary_key': 'True'}),
            'chapter': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'})
        },
        u'publishing.catalogue': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'Catalogue', '_ormbases': [u'publishing.Book']},
            u'book_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Book']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'publishing.coadvisorship': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Coadvisorship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishing.Thesis']"})
        },
        u'publishing.conference': {
            'Meta': {'ordering': "['acronym', 'name']", 'object_name': 'Conference'},
            'acronym': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256', 'db_index': 'True'})
        },
        u'publishing.conferencearticle': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'ConferenceArticle', '_ormbases': [u'publishing.Publication']},
            'crossref': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishing.ConferenceProceedings']", 'null': 'True', 'blank': 'True'}),
            'presentation': ('django.db.models.fields.files.FileField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'publication_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Publication']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'publishing.conferenceedition': {
            'Meta': {'ordering': "['-year', '-month', 'conference__acronym', 'conference__name']", 'unique_together': "(('conference', 'year'),)", 'object_name': 'ConferenceEdition'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishing.Conference']"}),
            'edition_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '512'}),
            'web_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'db_index': 'True'})
        },
        u'publishing.conferenceproceedings': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'ConferenceProceedings', '_ormbases': [u'publishing.Book']},
            u'book_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Book']", 'unique': 'True', 'primary_key': 'True'}),
            'conference_edition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishing.ConferenceEdition']"})
        },
        u'publishing.editorship': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Editorship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishing.Book']"})
        },
        u'publishing.exhibition': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'Exhibition', '_ormbases': [u'publishing.Publication']},
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'medium': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'publication_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Publication']", 'unique': 'True', 'primary_key': 'True'}),
            'show': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'publishing.journal': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'Journal', '_ormbases': [u'publishing.Book']},
            u'book_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Book']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'publishing.journalarticle': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'JournalArticle', '_ormbases': [u'publishing.Publication']},
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishing.Journal']"}),
            u'publication_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Publication']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'publishing.masterthesis': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'MasterThesis', '_ormbases': [u'publishing.Thesis']},
            u'thesis_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Thesis']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'publishing.phdthesis': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'PhdThesis', '_ormbases': [u'publishing.Thesis']},
            'reviewers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'reviewed_phdtheses'", 'to': u"orm['people.Person']", 'through': u"orm['publishing.Reviewing']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            u'thesis_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Thesis']", 'unique': 'True', 'primary_key': 'True'})
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
            'listed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'month': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '512'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'db_index': 'True'})
        },
        u'publishing.reviewing': {
            'Meta': {'object_name': 'Reviewing'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishing.PhdThesis']"})
        },
        u'publishing.technicalreport': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'TechnicalReport', '_ormbases': [u'publishing.Publication']},
            'institution': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['organizations.Institution']", 'symmetrical': 'False'}),
            u'publication_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Publication']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'publishing.thesis': {
            'Meta': {'ordering': "['-year', '-month']", 'object_name': 'Thesis', '_ormbases': [u'publishing.Publication']},
            'advisors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'advised_theses'", 'symmetrical': 'False', 'through': u"orm['publishing.Advisorship']", 'to': u"orm['people.Person']"}),
            'co_advisors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'coadvised_theses'", 'to': u"orm['people.Person']", 'through': u"orm['publishing.Coadvisorship']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            u'publication_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['publishing.Publication']", 'unique': 'True', 'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organizations.School']"})
        }
    }

    complete_apps = ['publishing']