from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:specie>/', views.detail, name='detail'),
]
