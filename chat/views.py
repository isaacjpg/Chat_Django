import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import caches, cache

from accounts.models import CustomUser
from .models import Room


@login_required
def index(request):
    users = CustomUser.objects.all()
    return render(request, 'chat/index.html', {'users': users})


@login_required
def private_room(request,to_user):
    to_user = CustomUser.objects.get(username=to_user)
   
    #Check if room exists
    room = Room.objects.filter(user1=request.user, user2=to_user).first()
    if not room:
        #check if room exists with user1 and user2 inverted
        room = Room.objects.filter(user1=to_user, user2=request.user).first()
        if not room:
            #create room
            room = Room.objects.create(user1=request.user, user2=to_user)

    #Get chached messages from room
    chached_messages = caches['default'].get(room.id)
    if not chached_messages:
        chached_messages = []
    else:
        chached_messages = json.loads(chached_messages)

    return render(request, 'chat/private_room.html', {
        'username': request.user.username,
        'to_user': to_user.username,
        'room_id': room.id,
        'messages': chached_messages
    })

