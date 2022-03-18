from django.urls import path 
from . import views

# base app urls
urlpatterns:list = [
    path('', views.index, name ='home'),

    path('room/<str:pk>', views.room, name ='room'),
    path('create-room/', views.createRoom, name ='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name ='update-room'),
]
