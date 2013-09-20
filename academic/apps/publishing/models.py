from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from django_countries.fields import CountryField

from model_utils.managers import InheritanceManager

from academic.settings import *
from academic.utils import *
from academic.apps.organizations.models import *
from academic.apps.people.models import *


class Conference(models.Model):
    class Meta:
        ordering = [
            'acronym',
            'name', ]
        
    name = models.CharField(
        _('Name'),
        help_text=_('E.g., Recent Advances in Intrusion Detection'),
        max_length=256,
        unique=True,
        db_index=True)
    acronym = models.CharField(
        max_length=16,
        unique=True,
        help_text=_('E.g., RAID, IMC, EC2ND, CCS, SSP'),
        validators=[RegexValidator(regex=r'^([0-9A-Za-z]+[ ]?)+$')])

    def __unicode__(self):
        return self.name

    def _get_acronymized(self):
        return u'%s (%s %s)' % (
            self.name,
            self.acronym)
    acronymized = property(_get_acronymized)


class ConferenceEdition(models.Model):
    class Meta:
        ordering = [
            '-year',
            '-month',
            'conference__acronym',
            'conference__name',]
        unique_together = (
            'conference',
            'year',)
    
    conference = models.ForeignKey(
        Conference)
    edition_number = models.PositiveSmallIntegerField(
        help_text=_('E.g., "13" as in "Proceedings of the 13th Symposioum on ..."'),
        blank=True,
        null=True,
        db_index=True)
    month = models.PositiveSmallIntegerField(
        choices=MONTHS,
        blank=True,
        null=True,
        db_index=True)
    year = models.CharField(
        max_length=4,
        choices=YEARS,
        help_text=_('Year of the event'),
        db_index=True)
    address = models.TextField(
        _('Venue'),
        help_text=_('Conference location.'),
        blank=True,
        null=True)
    web_page = models.URLField(
        _('Web page'),
        blank=True,
        null=True)
    slug = models.SlugField(
        max_length=512,
        editable=False,
        db_index=True)

    def __unicode__(self):
        return u'%s %s' % (self.conference, self.year)

    def _get_acronymized(self):
        return u'%s (%s %s)' % (
            self.conference.name,
            self.conference.acronym,
            self.year)
    acronymized = property(_get_acronymized)

    def _get_rev_acronymized(self):
        return u'%s %s - %s' % (
            self.conference.acronym,
            self.year,
            self.conference.name)
    rev_acronymized = property(_get_rev_acronymized)

    def save(self, **kwargs):
        if len(self.slug) == 0:
            self.slug = slugify('%s %s' % (self.conference.acronym, self.year))
        super(ConferenceEdition, self).save(**kwargs)


class Publication(models.Model):
    """
    A scientific publication.
    """
    
    class Meta:
        unique_together = (
            ('title',
             'year'), )
        verbose_name = _('Publication')
        verbose_name_plural = _('Publications')
        ordering = [
		'-year',
		'-month']
    
    title = models.CharField(
        _('Title'),
        max_length=1024)
    year = models.CharField(
        max_length=4,
        choices=YEARS,
        help_text=_('Year of publication'),
        db_index=True)
    month = models.PositiveSmallIntegerField(
        choices=MONTHS,
        db_index=True,
        null=True,
        blank=True)
    authors = models.ManyToManyField(
        Person,
        related_name='publications',
        through='Authorship',
        blank=True,
        null=True)
    attachment = models.FileField(
        _('Attachment'),
	upload_to=PUBLISHING_DEFAULT_DIRECTORY,
        max_length=256,
        blank=True,
        null=True)
    notes = models.CharField(
        _('Notes'),
        max_length=512,
        help_text=_('Notes, e.g., about the conference or the journal.'),
        blank=True,
        null=True)
    bibtex = models.TextField(
        verbose_name=_('BibTeX Entry'),
        help_text=_(
            'At this moment, the BibTeX is not parsed for content.'\
                'In the future, this will override the (not-yet-)auto-generated'\
                ' BibTeX.'),
        blank=True,
        null=True)
    abstract = models.TextField(
        _('Abstract'),
        blank=True,
        null=True)
    fulltext = models.FileField(
        _('Fulltext'),
	upload_to=PUBLISHING_DEFAULT_DIRECTORY,
        max_length=256,
        blank=True,
        null=True)
    date_updated = models.DateField(
        _('Last updated on'),
        auto_now=True,
        db_index=True)
    slug = models.SlugField(
        help_text=_('This is autofilled, then you may modify it if you wish.'),
        editable=False,
        unique=True,
        max_length=512,
        db_index=True)
    
    objects = InheritanceManager()

    def _get_first_author(self):
        authorships = self.authorship_set.all()
        if authorships.count() > 0:
            return authorships[0].person
        return None
    first_author = property(_get_first_author)

    def _get_author_list(self):
        author_list = ', '.join(map(
                lambda m:m.person.name , self.authorship_set.all()))
        return author_list
    author_list = property(_get_author_list)

    @models.permalink
    def get_bibtex_url(self):
        return ('academic_publishing_publication_detail_bibtex', (), {
                'slug': self.slug})

    @models.permalink
    def get_absolute_url(self):
        return ('academic_publishing_publication_detail', (), {'slug': self.slug})

    def __unicode__(self):
        return u'%s %s' % (
            self.title,
            self.year)

    def save(self, *args, **kwargs):
        if len(self.slug) == 0:
            self.slug = slugify('%s %s %s' % (
                    self.first_author or '',
                    self.title,
                    self.year))
        super(Publication, self).save(**kwargs)


class Authorship(models.Model):
    class Meta:
        ordering = ('order',)
    person = models.ForeignKey(Person)
    publication = models.ForeignKey(Publication)
    order = models.PositiveSmallIntegerField()
    

class Book(Publication):
    editors = models.ManyToManyField(
        Person,
        related_name='proceedings',
        through='Editorship',
        blank=True,
        null=True)
    publisher = models.ForeignKey(
        Publisher,
        related_name='books',
        blank=True,
        null=True)
    volume = models.CharField(
        max_length=128,
        blank=True,
        null=True)
    number = models.CharField(
        max_length=128,
        blank=True,
        null=True)
    address = models.TextField(
        _('Address'),
        help_text=_('Conference location.'),
        blank=True,
        null=True)
    edition = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        help_text=_('E.g., First, Second, II, 2, Second edition.'))

    def _get_editor_list(self):
        editor_list = ', '.join(map(
                lambda m:m.person.name , self.editorship_set.all()))
        return editor_list
    editor_list = property(_get_editor_list)

    def __unicode__(self):
        n = u'%s %s' % (self.title, self.year)
        if self.volume:
            n += ', vol. %s' % self.volume
        if self.number:
            n += ', no. %s' % self.number
        if self.edition:
            n += ' (%s)' % self.edition
        return n

class Editorship(models.Model):
    class Meta:
        ordering = ('order',)
    person = models.ForeignKey(Person)
    publication = models.ForeignKey(Book)
    order = models.PositiveSmallIntegerField()


class Journal(Book):
    pass

class BookChapter(Book):
    chapter = models.CharField(
        max_length=128)
    pages = models.CharField(
        blank=True,
        null=True,
        max_length=32,
        help_text=_('E.g., 12-20'),
        validators=[RegexValidator(regex=r'[0-9]+\-[0-9]+')])


class JournalArticle(Publication):
    class Meta:
        verbose_name_plural = _('Journal papers')
        verbose_name = _('Journal paper')
    
    journal = models.ForeignKey(
        Journal)


class ConferenceProceedings(Book):
    class Meta:
        verbose_name = _('Proceedings')
        verbose_name_plural = _('Proceedings')
    conference_edition = models.ForeignKey(
        ConferenceEdition)

    def __unicode__(self):
        return u'%s (proceedings)' % self.conference_edition.rev_acronymized


class ConferenceArticle(Publication):
    class Meta:
        verbose_name_plural = _('Conference papers')
        verbose_name = _('Conference paper')
    presentation = models.FileField(
        _('Presentation'),
	upload_to=PUBLISHING_DEFAULT_DIRECTORY,
        max_length=256,
        blank=True,
        null=True)
    crossref = models.ForeignKey(
        ConferenceProceedings,
        verbose_name=_('Conference proceedings'),
        null=True,
        blank=True)


class TechnicalReport(Publication):
    institution = models.ManyToManyField(
        Institution)


class Thesis(Publication):
    school = models.ForeignKey(
        School)
    advisors = models.ManyToManyField(
        Person,
        through='Advisorship',
        related_name='advised_theses')
    co_advisors = models.ManyToManyField(
        Person,
        through='Coadvisorship',
        blank=True,
        null=True,
        related_name='coadvised_theses')


class Advisorship(models.Model):
    class Meta:
        ordering = ('order',)
    person = models.ForeignKey(Person)
    publication = models.ForeignKey(Thesis)
    order = models.PositiveSmallIntegerField()


class Coadvisorship(models.Model):
    class Meta:
        ordering = ('order',)
    person = models.ForeignKey(Person)
    publication = models.ForeignKey(Thesis)
    order = models.PositiveSmallIntegerField()


class MasterThesis(Thesis):
    class Meta:
        verbose_name_plural = 'Master theses'
        verbose_name = 'Master thesis'
    pass


class PhdThesis(Thesis):
    class Meta:
        verbose_name_plural = _('PhD theses')
        verbose_name = _('PhD thesis')
    reviewers = models.ManyToManyField(
        Person,
        through='Reviewing',
        related_name='reviewed_phdtheses',
        blank=True,
        null=True)


class Reviewing(models.Model):
    person = models.ForeignKey(Person)
    publication = models.ForeignKey(PhdThesis)
    order = models.PositiveSmallIntegerField()
