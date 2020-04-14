from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy

from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):   # **kwargs means it can take multiple arguments and retunrs as a dictionary , with keywords
        context=super().get_context_data(**kwargs)
        context['injectme']='BASIC INJECTION FROM CLASSS BASED VIEW'
        return context

#This is sample list view
class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'  ## it is used in html file , by default it will be the lowercase of your model name
    template_name = 'basic_app/school_list.html'

#This is sample details view
class SchoolDetailsView(DetailView):
    model = models.School
    template_name = 'basic_app/school_details.html'
    context_object_name='school_details'   ## it is used in html file

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name','principal','location')

class StudentCreateView(CreateView):
    model = models.Students
    fields = ('student_name','age','school')

class StudentCreateSuccess(TemplateView):
    template_name = 'basic_app/student_created_succcess.html'

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name','principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")