from django.urls import path

from . import views

app_name = 'rice4869'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:gene_id>/', views.detail, name='detail'),
    path('<str:gene_id>/network/', views.network, name='network')
]
