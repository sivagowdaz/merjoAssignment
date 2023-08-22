from django.urls import path  
from .views import registerUser, authenticate

urlpatterns = [
    path('register/', registerUser, name='register user'),
    path('authenticate/', authenticate, name='authenticate user'),
]