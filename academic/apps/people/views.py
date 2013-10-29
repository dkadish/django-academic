# for some reason, switching to class-based views causes crazy things
# with {{ object_list|regroup }}. Thus, let's stick to the old
# approach for now.

from django.views.generic.list import ListView

from .models import Person

class PeopleListView(ListView):
    queryset = Person.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(PeopleListView, self).get_context_data(**kwargs)
        context['visitors_list'] = Person.objects_visitors.all()
        return context
    
class PastPeopleListView(PeopleListView):
    queryset = Person.objects_past.all()
    
    def get_context_data(self, **kwargs):
        context = super(PeopleListView, self).get_context_data(**kwargs)
        context['visitors_list'] = Person.objects_past_visitors.all()
        context['past'] = True
        return context