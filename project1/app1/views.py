from django.shortcuts import render 
from .models import *
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer
from rest_framework import status, filters
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins, viewsets


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
    
class CVB_pf(APIView):
    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    def get (self, request, pk): 
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response (serializer.data)
    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
        
    def delete(self, request, pk): 
        guest = self.get_object(pk)
        guest.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
# Mixins 
class mixins_list(mixins.ListModelMixin, mixins.CreateModelMixin,  generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    def get(self, request): 
        return self.list(request)
    def post(self, request):
        return self.create(request) 
    
class Mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):  # Changed from post to put for update
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
    
class Generics_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class Generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

# 7 viewsets
class viewset_guest(viewsets.ModelViewSet): 
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class viewsets_movie(viewsets.ModelViewSet): 
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backend = [filters.SearchFilter]
    search_fields  = ['movie']

class viewsets_reservation(viewsets.ModelViewSet): 
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

#Find movie
@api_view(['GET'])
def find_movie(request):
    movie = request.GET.get('movie')  
    hall = request.GET.get('hall')    

    if not movie or not hall:
        return Response({"error": "Both 'movie' and 'hall' parameters are required."}, status=400)

    movies = Movie.objects.filter(movie=movie, hall=hall)
    serializer = MovieSerializer(movies, many=True)
    
    return Response(serializer.data)


#Create new resrvation
@api_view(['POST'])
def new_resrvation(request): 
    movie = Movie.objects.get(
        movie = request.data['movie'], 
        hall = request.data['hall'] 
    )
    guest = Guest()
    guest.name = request.data['name']
    guest.mobile = request.data['mobile']
    guest.save() 

    reservation = Reservation()
    reservation.guest = guest
    reservation.movie = movie
    reservation.save() 

    return Response(status = status.HTTP_201_CREATED)