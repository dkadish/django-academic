from django.conf.urls.defaults import *
from django.views.decorators.cache import cache_page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import *

urlpatterns = patterns(
    '',

#     url(r'^topics/(?P<slug>[-\w]+)/$',
#         cache_page(object_detail),
#         {'template_name': 'academic/topic_detail.html',
#          'queryset': Topic.objects.all() },
#         name='academic_projects_topic_detail'),
# 
#     url(r'^topics/$',
#         cache_page(object_list),
#         {'template_name': 'academic/topic_list.html',
#          'queryset': Topic.objects.all() },
#         name='academic_projects_topic_list'),
#         
    url(r'^(?P<slug>[-\w]+)/$',
        DetailView.as_view(
                queryset=Project.objects.all(),
                template_name='academic/project_detail.html'
                           ),
        name='academic_projects_project_detail'),

    url(r'^$',
        ListView.as_view(
                queryset=Project.objects.order_by('topic'),
                template_name='academic/project_list.html'),
        name='academic_projects_project_list'),
)

