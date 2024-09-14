from django.shortcuts import render 
from .models import *
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer
from rest_framework import status, filters
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

def no_rest_no_model(request):
    guests = [
        {
            'id': 1, 
            'name': "Hamada", 
            'mobile': "12345",  
        },
        {
            'id': 2, 
            'name': "Nehal", 
            'mobile': "25354",  
        },
    ]
    return JsonResponse(guests, safe=False) 

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
        serializer = GuestSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['GET', 'PUT', 'DELETE']) 
def FBV_pk(request, pk): 
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method == 'GET': 
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    #PUT
    elif request.method == 'PUT':
        serializer = GuestSerializer(guest, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #DELETE
    if request.method == 'DELETE':
        guest.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 
    
# CBV : class based views 

class CVB_List(APIView): 
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many= True)
        return Response(serializer.data)
    def post(self, request): 
        serializer = GuestSerializer(date = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else: 
            return Response (serializer.data, status = status.HTTP_200_BAD_REQUEST)