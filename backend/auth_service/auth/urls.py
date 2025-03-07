from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView, 
    LoginView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    EmailConfirmationView
    )


urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='auth-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-rest-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('email-confirmation/', EmailConfirmationView.as_view(), name='email-confirmation'),
]
