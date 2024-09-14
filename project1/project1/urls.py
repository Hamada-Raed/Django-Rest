
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/jsonresponsemomodel/', views.no_rest_no_model),
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),
    path('django/FBV_List/', views.FBV_List),   # List view, no pk argument
    path('django/FBV_pk/<int:pk>/', views.FBV_pk),  # Detail view with pk argument
    path('django/CVB_List/', views.CVB_List.as_view()),
]
