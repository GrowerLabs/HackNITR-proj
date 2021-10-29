from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from . models import Chat
# Create your views here.
def index(request):
    if request.method == 'POST':
        room = request.POST.get('room')
        try:
            get_room = Chat.objects.filter(room_name = room)
        except:
            return redirect("/")

        if get_room:
            c = get_room[0]
            number = c.allowed_users

            if int(number) <2:
                number = 2
                return redirect(f'/video/{room}/join/')
        else:
            return redirect("/")

    return render(request, 'chat/index.html')

def video(request, room, created):
    return render(request, 'chat/meet.html',{
        'created': created,
        'room': room
    })


def new_meet(request):
    create = Chat.objects.create(allowed_users =1)
    if create:
        return redirect(f'/video/{create.room_name}/created/')

    return redirect("/")


def close_meet(request,room, created):
    print(created)
    if created == "created":
        room_ = get_object_or_404(Chat,room_name=room )
        print(room_)
        room_.delete()
        

    return redirect("/")
