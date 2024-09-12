from django.shortcuts import render
from django.http.response import JsonResponse, Response 
from .models import *
from rest_framework.decorators import api_view
from .serializers import GuestSerializer, MovieSerializer , ReservationSerializer



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

# no rest-f form model 
def no_rest_from_model(request): 
    data = Guest.objects.all() 
    response = {
        'guests' : list(data.values('name', 'mobile'))
    }    
    return JsonResponse(response)

@api_view(['GET', 'POST']) 
def FBV_List(request):
    if request.method == 'GET':
        guests = Guest.objects.all() 
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)