from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

class SchoolListView(LoginRequiredMixin, ListView):
    model = School
    # Default would be 'school_list'
    # Example of making your own:
    # context_object_name = 'schools'
    
class SchoolDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'school_details'
    model = School
    template_name = 'schools_app/school_detail.html'


class SchoolCreateView(LoginRequiredMixin,CreateView):
    fields = ("name","principal","location")
    model = School


class SchoolUpdateView(LoginRequiredMixin,UpdateView):
    fields = ("name","principal")
    model = School

class SchoolDeleteView(LoginRequiredMixin,DeleteView):
    model = School
    success_url = reverse_lazy("schools_app:school_list")

