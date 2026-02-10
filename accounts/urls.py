from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    # Add <str:pk> to the URL. 'pk' stands for Primary Key (ID)
    path('customer/<str:pk>/', views.customer, name="customer"),
]