
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('roomView/', RoomView.as_view()),
    path('roomViewList/', RoomView_List.as_view()),
    
]
