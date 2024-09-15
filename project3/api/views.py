from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics 
from .models import *
from .serializers import *

#THIS FUNCTION TO TEST THE CODE AND MAKE SURE EVERYTHING IS GOOD. 
def main(request): 
    return HttpResponse('<h1>Hello</h1>')

#POST METHOD TO ADD ROOMS. 
class RoomView(generics.CreateAPIView): 
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

#GET METHOD TO SHOW ROOMS.
class RoomView_List(generics.ListAPIView): 
    queryset = Room.objects.all()
    serializer_class = RoomSerializer