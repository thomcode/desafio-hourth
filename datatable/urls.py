from django.urls import path
from . import views

urlpatterns = [
    path('', views.datatable, name='datatable'),
    path('api/', views.api_datatable, name='api_datatable'),
]