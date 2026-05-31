from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("questionnaire/", views.question, name="question"),
    path("confirmation/", views.confirm, name="confirm"),
]