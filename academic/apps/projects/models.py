from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from academic.utils import *

from academic.apps.content.models import *
from academic.apps.people.models import *
from academic.apps.publishing.models import *

class HighlightedTopicManager(models.Manager):
    def get_query_set(self):
        return super(HighlightedTopicManager, self).get_query_set().filter(
            highlight=True).order_by('highlight_order')


class Topic(models.Model):
    class Meta:
        ordering = [
            'title']

    objects = models.Manager()
    highlighted = HighlightedTopicManager()
    
    highlight = models.BooleanField(
        default=False,
        help_text='Show this topic on the home page?',
        db_index=True)
    highlight_order = models.PositiveSmallIntegerField(
        default=0,
        help_text='In what order do you want this to be added on the home page?'\
            ' Leave blank for alphabetic order.',
        db_index=True)
    title = models.CharField(
        max_length=2048,
        db_index=True)
    slug = models.SlugField(
	max_length=128,
	db_index=True)
    excerpt = models.TextField(
        null=True,
        blank=True)
    description = models.TextField()

    def _get_content(self):
        if self.excerpt:
            return self.excerpt
        return self.description
    content = property(_get_content)

    @models.permalink
    def get_absolute_url(self):
        return ('academic_projects_topic_detail', (), {'slug': self.slug})

    def __unicode__(self):
        return self.title


class HighlightedProjectManager(models.Manager):
    def get_query_set(self):
        return super(HighlightedProjectManager, self).get_query_set().filter(
            highlight=True)


class Project(models.Model):
    class Meta:
        ordering = [
            '-start_year',
            '-presented_year',
            '-end_year']

    objects = models.Manager()
    highlighted = HighlightedProjectManager()
    
    highlight = models.BooleanField(
        help_text='Highlight this in the projects\' main page?'\
            ' Only the most recently modified one will be displayed.')
    redirect_to = models.URLField(
        blank=True,
        null=True,
        help_text='Use this for old or extenal projects.')
    short_title = models.CharField(
        max_length=1024,
        db_index=True)
    slug = models.SlugField(
	max_length=128,
	db_index=True)
    title = models.CharField(
        max_length=2048,
        db_index=True)
    created = models.DateTimeField(
        auto_now_add=True)
    modified = models.DateTimeField(
        auto_now=True)
    start_year = models.SmallIntegerField(default=2000, help_text='The year in which the project was started.')
    end_year = models.SmallIntegerField(default=2000, help_text='The year in which the project was finished.')
    presented_year = models.SmallIntegerField(default=2000, help_text='The year in which the project was shown for the first time.')
    excerpt = models.CharField(
        max_length=1024,
        null=True,
        blank=True,
        help_text='Concise description to show in the listing page.')
    description = models.TextField(
        null=True,
        blank=True,
        help_text='This content will be rendered right after the title.')
    downloads = models.ManyToManyField(
        Download,
        null=True,
        blank=True,
        help_text='Downloadable files')
    footer = models.TextField(
        null=True,
        blank=True,
        help_text='This content will be rendered at the bottom of the page.')
    people = models.ManyToManyField(
        Person,
        help_text='People involved in this project.',
        related_name='projects',
        through='Involvement',
        blank=True,
        null=True)
    organizations = models.ManyToManyField(
        Organization,
        help_text='Organizations involved other than the lab.',
        blank=True,
        null=True,
        related_name='projects')
    publications = models.ManyToManyField(
        Publication,
        blank=True,
        null=True)
    topic = models.ForeignKey(
        Topic,
        verbose_name=_('Main topic'),
        help_text='This is the main topic.',
        related_name='projects')
    sponsors = models.ManyToManyField(
        Sponsor,
        blank=True,
        null=True,
        help_text='sponsored_projects')
    related_topics = models.ManyToManyField(
        Topic,
        null=True,
        blank=True,
        help_text='Optional related topics.',
        related_name='secondary_projects')
    image = models.ImageField(
        upload_to='cover_images',
        verbose_name=_('Cover Image'),
        help_text='An image to display with the project.',
        null=True,
        blank=True)
    image_caption = models.TextField(
        null=True,
        blank=True)
    
    @property
    def involvements(self):
        return Involvement.objects.filter(project=self)

    def __unicode__(self):
        return self.short_title

    @models.permalink
    def get_absolute_url(self):
        return ('academic_projects_project_detail', (), {'slug': self.slug})


class Role(models.Model):
    class Meta:
        ordering = ('order',)
        
    name = models.CharField(
        _('Role name'),
        help_text=_('E.g., Project Leader'),
        max_length=64)
    plural_name = models.CharField(
        _('Role plural name'),
        help_text=_('E.g., Project Leaders'),
        max_length=64)
    order = models.PositiveSmallIntegerField(
        _('Role order'),
        help_text=_('Lower values mean higher importance.'
                    ' I.e., put 0 for a "Project Leader"'),
        default=0)

    def __unicode__(self):
        return self.name

class Involvement(models.Model):
    class Meta:
        ordering = ('role', 'order',)
    
    project = models.ForeignKey(Project)
    person = models.ForeignKey(Person)
    role = models.ForeignKey(Role)
    order = models.PositiveSmallIntegerField()
    
    def __unicode__(self):
        return '%s - %s - %s' %(self.project, self.person, self.role)
