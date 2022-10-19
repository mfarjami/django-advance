from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = "api-v1"

urlpatterns = [
    # Auth token
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDisCardAuthToken.as_view(), name='token-logout'),

    path('change-password/',views.ChangePasswordApiView.as_view(),name='change-password'),
    path('profile/', views.ProfileApiView.as_view(), name='profile'),
    
    # JWT token
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]