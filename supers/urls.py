from django.urls import path
from . import views

urlpatterns = [
    path("", views.supers_detail ), 
    path("<int:pk>/", views.super_detail),  # int
]
