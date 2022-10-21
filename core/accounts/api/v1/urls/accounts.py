from django.urls import path, include
from .. import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    # Auth token
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDisCardAuthToken.as_view(), name='token-logout'),

    path('change-password/',views.ChangePasswordApiView.as_view(),name='change-password'),
    
    path("activation/confirm/<str:token>", views.ActivationApiView.as_view(), name="activation"),
    path('activation/resend/', views.ActivationResendApiView.as_view(), name='activation-resend'),
    # JWT token
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]