from base.models import Task
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
class TastList(ListView):
    model = Task
    context_object_name = 'tasks'
