from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('private/<str:to_user>/', views.private_room, name='private_room')
]
