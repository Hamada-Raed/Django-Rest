from django.shortcuts import render 
from .models import *
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer
from rest_framework import status, filters

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

def no_rest_no_model(request):
    guests = [
        {
            'id': 1,  # Added missing comma here
            'name': "Hamada", 
            'mobile': "12345",  # Changed to string for consistency
        },
        {
            'id': 2, 
            'name': "Nehal", 
            'mobile': "25354",  # Fixed the typo here and changed to string
        },
    ]
    return JsonResponse(guests, safe=False) 

# No REST and no model query
def no_rest_from_model(request): 
    data = Guest.objects.all() 
    response = {
        'guests': list(data.values('name', 'mobile'))
    }    
    return JsonResponse(response)

@api_view(['GET', 'POST']) 
def FBV_List(request):
    if request.method == 'GET':
        guests = Guest.objects.all() 
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)  # Fixed typo from 'date' to 'data'
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid
