# app1/admin.py
from django.contrib import admin
from .models import Guest, Movie, Reservation

# Ensure each model is registered only once
admin.site.register(Guest)
admin.site.register(Movie)
admin.site.register(Reservation)
