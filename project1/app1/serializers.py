from rest_framework import serializers
from app1.models import Guest, Movie, Reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    # Use ReservationSerializer to include the reservation details
    reservation = ReservationSerializer(many=True, read_only=True, source='reservation_set')

    class Meta:
        model = Guest
        fields = ['pk', 'name', 'mobile', 'reservation']
