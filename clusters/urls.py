from django.urls import path

from . import views

app_name = 'clusters'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:species>/', views.detail, name='detail'),
]
