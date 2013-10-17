from django.views.generic.list import ListView
from django.db.models import Count
from django.core.cache import cache

from .models import Publication
from ..people.models import Person

import datetime
from .models import Book, JournalArticle, ConferenceArticle,\
    Exhibition, Catalogue, Thesis

class PublicationListView(ListView):
    template_name = 'academic/publication_list.html'
    current_year = datetime.datetime.now().year
    publication_stats = cache.get('publication_stats')
    top_authors = cache.get('top_authors')
    
#     def get_queryset(self):
#         return Publication.objects.exclude(
#             real_type__name='conference proceedings').exclude(
#             real_type__name='journal')

    def get_top_authors(self):
        if self.top_authors is None:
            self.top_authors = Person.objects.annotate(
                papers=Count('publications')).filter(
                papers__gt=0).order_by('-papers')[0:5]
            cache.set('top_authors', self.top_authors)
        return self.top_authors

    def get_publications_stats(self):
        publications = self.get_queryset()
        if self.publication_stats is None:
            self.publication_stats = publications.values('year').annotate(
                papers=Count('year'))

            if self.publication_stats:
                self.publication_stats = dict(
                    (int(x['year']), int(x['papers'])) \
                        for x in self.publication_stats)
                
                first_year = max(
                    self.publication_stats.keys()[-1],
                    self.current_year - 10)

                last_year = max(
                    self.publication_stats.keys()[0],
                    self.current_year)

                for y in xrange(first_year, last_year+1):
                    if y not in self.publication_stats:
                        self.publication_stats[y] = 0
                self.publication_stats = {
                    'years': [str(y)[-2:] for y in self.publication_stats.keys()],
                    'values': self.publication_stats.values()}
            cache.set('publication_stats', self.publication_stats)
        return self.publication_stats

    def get_context_data(self, **kwargs):
        context = super(PublicationListView, self).get_context_data(**kwargs)
        context['publication_stats'] = self.get_publications_stats()
        context['top_authors'] = self.get_top_authors()
        return context

class PublicationListByTypeView(ListView):
    template_name = 'academic/publication_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(PublicationListByTypeView, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.filter(listed=True)
        context['journal_article_list'] = JournalArticle.objects.filter(listed=True)
        context['conference_article_list'] = ConferenceArticle.objects.filter(listed=True)
        context['exhibition_list'] = Exhibition.objects.filter(listed=True)
        context['catalogue_list'] = Catalogue.objects.filter(listed=True)
        context['thesis_list'] = Thesis.objects.filter(listed=True)
        return context