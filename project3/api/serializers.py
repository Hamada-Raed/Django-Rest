from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at']
