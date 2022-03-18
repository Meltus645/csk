from django.urls import path
from django.views import View
from . import views

# base app urls
urlpatterns:list = [
    path('', views.index, name ='home'),
]
