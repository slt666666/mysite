from django.urls import path

from . import views

app_name = 'rice4869'
urlpatterns = [
    path('', views.index, name='index'),
]
