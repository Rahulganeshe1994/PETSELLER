
from django.urls import path,include
from home.views import *
urlpatterns = [
    
    path('animal/',AnimalView.as_view()),
]