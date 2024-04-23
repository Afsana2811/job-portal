from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
   
    path('register/', views.sign_up, name='register'),
    path('list/', views.list, name= 'list'),
    path('customer/', views.customer),
]