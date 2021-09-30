from django.urls import path
from . import views

urlpatterns = [
    path('', views.tastList, name='tasks')
]