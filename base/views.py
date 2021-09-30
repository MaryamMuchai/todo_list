from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tastList(request):
    return HttpResponse('To Do List')
