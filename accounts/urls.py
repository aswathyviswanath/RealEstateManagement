from django.urls import path
from .views import RegisterAPIView, LoginAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),


]
