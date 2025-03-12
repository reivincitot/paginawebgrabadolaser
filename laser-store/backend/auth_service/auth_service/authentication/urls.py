from django.urls import path
from authentication.views import GoogleLogin, FacebookLogin

urlpatterns = [
    path('auth/google/', GoogleLogin.as_view(), name='google-login'),
    path('auth/facebook/', FacebookLogin.as_view(), name='facebook-login'),
]
