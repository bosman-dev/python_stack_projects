from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models

class SchoolListView(ListView):
    model = models.School
    # Default would be 'school_list'
    # Example of making your own:
    # context_object_name = 'schools'
    
class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")

