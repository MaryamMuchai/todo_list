from django.urls import path
from .views import TastList

urlpatterns = [
    path('', TastList.as_view(), name='tasks'),
]