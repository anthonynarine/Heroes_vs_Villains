from django.urls import path
from . import views

urlpatterns = [
    path("", views.supers_detail), 
    path("<int:pk>/", views.super_pk_needed),  # int
#     path("", views.supers_and_types),  # int
]
