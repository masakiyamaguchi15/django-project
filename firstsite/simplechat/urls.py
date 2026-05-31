from django.urls import path
from . import views

app_name = 'simplechat'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post_create, name='post'),
    path('list/', views.post_list, name='post_list'),
]
