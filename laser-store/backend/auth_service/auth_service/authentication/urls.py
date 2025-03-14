from django.urls import path
from authentication.views import GoogleLogin, FacebookLogin, RegisterView, LoginView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('auth/google/', GoogleLogin.as_view(), name='google-login'),
    path('auth/facebook/', FacebookLogin.as_view(), name='facebook-login'),
]
