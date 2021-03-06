from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from django_countries.fields import CountryField

from datetime import date

from academic.settings import *
from academic.utils import *
from academic.apps.organizations.models import *

class Rank(models.Model):
    """
    The academic rank (e.g., udergraduate student, graduate student,
    phd candidate, assistant professor)
    """
    class Meta:
        verbose_name = _('Rank')
        verbose_name_plural = _('Ranks')
        ordering = [
            'order',]

    name = models.CharField(
        _('Rank name'),
        help_text=_('E.g., Full Professor'),
        max_length=64)
    plural_name = models.CharField(
        _('Rank plural name'),
        help_text=_('E.g., Full Professors'),
        max_length=64)
    order = models.PositiveSmallIntegerField(
        _('Rank order'),
        help_text=_('Lower values mean higher importance.'
                    ' I.e., put 0 for a "Full professor"'))

    def __unicode__(self):
        return self.name


class AlumniManager(models.Manager):
    '''
    People who graduated here and left.
    '''
    def get_query_set(self):
        return super(AlumniManager, self).get_query_set().filter(
            alumni=True,
            public=True)


class VisitorManager(models.Manager):
    '''
    People who are visiting.
    '''
    def get_query_set(self):
        return super(VisitorManager, self).get_query_set().filter(
            current=True,
            visitor=True,
            public=True)


class PastVisitorManager(models.Manager):
    '''
    People who visited the lab in the past.
    '''
    def get_query_set(self):
        return super(PastVisitorManager, self).get_query_set().filter(
            visitor=True,
            current=False,
            public=True)

class PastTeamManager(models.Manager):
    '''
    People who visited the lab in the past.
    '''
    def get_query_set(self):
        return super(PastTeamManager, self).get_query_set().filter(
            current=False,
            visitor=False,
            alumni=False,
            public=True)

class PersonManager(models.Manager):
    '''
    Genuine people.
    '''
    def get_query_set(self):
        return super(PersonManager, self).get_query_set().filter(
            current=True,
            visitor=False,
            alumni=False,
            public=True).order_by('rank__order', 'first_name', 'last_name')
            #TODO: by existing meta

class Person(models.Model):
    """
    A person in a research lab.
    """
    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')
        unique_together = (
            'first_name',
            'mid_name',
            'last_name')
        ordering = [
            'rank',
            'last_name',
            'first_name', ]

    objects_all = models.Manager()
    objects_visitors = VisitorManager()
    objects_alumni = AlumniManager()
    objects_past_visitors = PastVisitorManager()
    objects_past = PastTeamManager()
    objects = PersonManager()

    listed = models.BooleanField(default=True, help_text='Should this person be listed publicly on the web site?')
    affiliation = models.ManyToManyField(
        Organization,
        verbose_name=_('Affiliations'),
        blank=True,
        null=True,
        related_name='people')
    public = models.BooleanField(
        verbose_name=_('Public?'),
        help_text=_('Toggle visibility on main pages.'),
        default=True)
    visitor = models.BooleanField(
        verbose_name=_('Visitor'),
        help_text=_('Is he/she a visitor?'),
        default=False)
    alumni = models.BooleanField(
        verbose_name=_('Alumni'),
        help_text=_('Did he/she graduate here?'),
        default=False)
    current = models.BooleanField(
        verbose_name=_('Current'),
        help_text=_('Is he/she still in the group?'),
        default=True)
    rank = models.ForeignKey(
        Rank,
        verbose_name=_('Academic Rank'),
        help_text=_('Leave blank if this person is not in the group anymore.'),
        related_name='people',
        blank=True,
        null=True)
    title = models.CharField(
        _('Title'),
        help_text=_('Non-academic title (e.g. Director of a lab, etc.)'),
        max_length=200,
        blank=True,
        null=True)
    first_name = models.CharField(
        _('First Name'),
        max_length=64)
    mid_name = models.CharField(
        blank=True,
        null=True,
        max_length=64)
    last_name = models.CharField(
        _('Last Name'),
        max_length=64)
    slug = models.SlugField(
        _('Slug'))
    e_mail = models.EmailField(
        _('E-mail'),
        blank=True,
        null=True)
    phone = models.CharField(
        _('Phone Number'),
        help_text='Phone number, using "-" as a separator (e.g. 123-456-7890)',
        max_length=64,
        blank=True,
        null=True)
    web_page = models.URLField(
        _('Web page'),
        blank=True,
        null=True)
    description = models.TextField(
        _('Short bio'),
        blank=True,
        null=True)
    picture = models.ImageField(
        _('Profile picture'),
        max_length=200,
	    upload_to=PEOPLE_DEFAULT_DIRECTORY,
        default=PEOPLE_DEFAULT_PICTURE,
        blank=True,
        null=True)

    @models.permalink
    def get_absolute_url(self):
        return ('academic_people_person_detail', (), {'slug': self.slug})

    def _get_picture_url(self):
        if self.has_picture:
            return str(self.picture)
        return PEOPLE_DEFAULT_PICTURE
    picture_url = property(_get_picture_url)

    def photo(self):
        if self.has_picture:
            return '<img src="%s" alt="%s">' % (
                self.picture.url,
                self.name)
        return _('(no photo)')
    photo.allow_tags = True

    def thumbnail(self):
        if self.has_picture:
            return '<img src="%s" alt="%s" style="max-width: 75px; max-height: 75px">' % (
                self.picture.url,
                self.name)
        return _('(no photo)')
    thumbnail.allow_tags = True

    def _has_picture(self):
        return not isinstance(self.picture.size, str) \
            and self.picture.size > 0
    has_picture = property(_has_picture)

    def __unicode__(self):
        return u'%s, %s' %(self.last_name, self.first_name)

    def _get_name(self):
        r = '%s' % self.first_name
        if self.mid_name:
            r = '%s %s.' % (r, self.mid_name[0])
        return '%s %s' % (r, self.last_name)
    name = property(_get_name)

    def _get_fullname(self):
        r = '%s' % self.first_name
        if self.mid_name:
            r = '%s %s' % (r, self.mid_name)
        return '%s %s' % (r, self.last_name)
    fullname = property(_get_fullname)

    def _get_sname(self):
        r = '%s.' % self.first_name[0]
        if self.mid_name:
            r = '%s %s.' % (r, self.mid_name[0])
        return '%s %s' % (r, self.last_name)
    sname = property(_get_sname)

    @staticmethod
    def autocomplete_search_fields():
        return ("first_name__icontains", "last_name_icontains",)

