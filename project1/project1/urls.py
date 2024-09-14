
from django.contrib import admin
from django.urls import path, include
from app1 import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('guests', views.viewset_guest)
router.register('movies', views.viewsets_movie)
router.register('reservation', views.viewsets_reservation)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/jsonresponsemomodel/', views.no_rest_no_model),
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),
    path('django/FBV_List/', views.FBV_List),   # List view, no pk argument
    path('django/FBV_pk/<int:pk>/', views.FBV_pk),  # Detail view with pk argument
    path('django/CVB_List/', views.CVB_List.as_view()),
    path('django/CVB_pf/<int:pk>', views.CVB_pf.as_view()), 
    path('django/mixins_list/', views.mixins_list.as_view()), 
    path('django/Mixins_pk/<int:pk>', views.Mixins_pk.as_view()), 
    path('django/Generics_list/', views.Generics_list.as_view()),
    path('django/Generics_list/', views.Generics_list.as_view()),
    path('django/Generics_pk/<int:pk>', views.Generics_pk.as_view()),
    path('django/viewset_guest/', include(router.urls)), #The easiest way.

    #find movie 
    path('fbv/findMovie/', views.find_movie),
    path('fvb/new_resrvation', views.new_resrvation), 
]
