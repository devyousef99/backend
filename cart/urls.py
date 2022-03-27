from django.urls import path
from .views import *
from cart import views

urlpatterns = [
    path('get_cart/<int:pk>', views.get_cart_usr),
]