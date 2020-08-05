from django.urls import path, include
from .views import UserCreate

urlpatterns = [
    path('register', UserCreate.as_view(), name='register'),
    path('rest-auth/', include('rest_auth.urls')),
]
