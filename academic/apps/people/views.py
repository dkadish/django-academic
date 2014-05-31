# for some reason, switching to class-based views causes crazy things
# with {{ object_list|regroup }}. Thus, let's stick to the old
# approach for now.

from django.views.generic.list import ListView

from .models import Person

DIRECTOR = 'Dulic'

class PeopleListView(ListView):
    queryset = Person.objects.exclude(last_name=DIRECTOR)
    
    def get_context_data(self, **kwargs):
        context = super(PeopleListView, self).get_context_data(**kwargs)
        context['visitors_list'] = Person.objects_visitors.all()
        context['directors_list'] = Person.objects.filter(last_name=DIRECTOR)
        return context
    
class StudentFacultyListView(PeopleListView):
    queryset = Person.objects.exclude(last_name=DIRECTOR)
    
    def get_context_data(self, **kwargs):
        context = super(StudentFacultyListView, self).get_context_data(**kwargs)
        context['directors_list'] = Person.objects.filter(last_name=DIRECTOR)
        context['faculty_list'] = self.queryset.exclude(last_name=DIRECTOR).filter(rank__name__contains='professor')
        context['students_list'] = self.queryset.exclude(last_name=DIRECTOR).filter(rank__name__contains='student')
        context['visitors_list'] = Person.objects_visitors.all()
        return context
    
class PastPeopleListView(PeopleListView):
    queryset = Person.objects_past.all()
    
    def get_context_data(self, **kwargs):
        context = super(PastPeopleListView, self).get_context_data(**kwargs)
        context['visitors_list'] = Person.objects_past_visitors.all()
        context['past'] = True
        return context
        
        
class PastStudentFacultyListView(StudentFacultyListView):
    queryset = Person.objects_past.all()
    
    def get_context_data(self, **kwargs):
        context = super(PastStudentFacultyListView, self).get_context_data(**kwargs)
        context['context'] = context.copy()
        context['visitors_list'] = Person.objects_past_visitors.all()
        context['past'] = True
        return context
