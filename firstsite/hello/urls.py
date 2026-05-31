from django.urls import path
from . import views

urlpatterns = [
    path("01/", views.hello), 
    path("02/", views.bye), 
]