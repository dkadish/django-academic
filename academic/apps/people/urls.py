from django.conf.urls.defaults import *
from django.views.decorators.cache import cache_page
# from django.views.generic.list_detail import object_list
from django.views.generic.list import ListView

from .models import *
from django.views.generic.detail import DetailView

urlpatterns = patterns(
    '',

    # switching to class-based views causes crazy things with {{
    # object_list|regroup }}. Thus, let's stick to the old approach for now.
                       
    url(r'^past/$',
        ListView.as_view(
                template_name='academic/person_list.html',
                model=Person),
        {
         'queryset': Person.objects_past.all(),
         'extra_context': {
                'past': True,
                'visitors': Person.objects_past_visitors.all().order_by('rank')} },
        name='academic_past_people_person_list'),

    url(r'^(?P<slug>[-\w\d]+)/$',
        DetailView.as_view(
                template_name='academic/person_detail.html',
                model=Person),
        name='academic_people_person_detail'),
                       
    url(r'^$',
        ListView.as_view(
                template_name='academic/person_list.html',
                model=Person),
        {
         'queryset': Person.objects.all(),
         'extra_context': {
                'visitors': Person.objects_visitors.all().order_by('rank'),
                },
        },
        name='academic_people_person_list'),
    
                       
)
