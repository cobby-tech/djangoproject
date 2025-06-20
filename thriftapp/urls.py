from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]