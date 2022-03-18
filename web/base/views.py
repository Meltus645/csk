from django.shortcuts import render 
from .models import Topic, Room 

# Create your views here.

def index(request):
    topics =Topic.objects.all()
    rooms =Room.objects.all()

    context:dict ={'rooms': rooms, 'topics': topics}
    return render(request, 'base/index.html', context)