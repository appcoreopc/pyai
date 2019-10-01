from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.


# def index(request):
# #     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    return render(request, 'devOpsApi/index.html', {})

def room(request, room_name):
    return render(request, 'devOpsApi/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })