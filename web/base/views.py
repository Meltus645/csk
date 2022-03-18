from django.shortcuts import render, redirect 
from .forms import RoomForm
from django.db.models import Q
from .models import Topic, Room 

# Create your views here.

def index(request):
    q =request.GET.get('q') if request.GET.get('q') != None else ''
    topics =Topic.objects.all()
    rooms =Room.objects.filter(
        Q(topic__name__icontains =q)|
        Q(name__icontains =q) |
        Q(description__icontains =q)
    )

    context:dict ={'rooms': rooms, 'topics': topics}
    return render(request, 'base/index.html', context)

def room(request, pk):
    room =Room.objects.get(id =pk) 
    participants =room.participants.all()
    context: dict ={'room': room, 'partcipants': participants}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form =RoomForm()
    if request.method =='POST':
        form =RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context ={'form': form}
    return render(request, 'base/room_form.html', context)    

def updateRoom(request, pk):
    room =Room.objects.get(id =pk)
    form =RoomForm(instance=room)
    if request.method =='POST':
        form =RoomForm(request.POST, instance =room)
        if form.is_valid():
            form.save() 
            return redirect('home') 
    context ={'form': form}
    return render(request, 'base/room_form.html', context)    