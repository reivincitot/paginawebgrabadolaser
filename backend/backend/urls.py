from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_framework_simplejwt.views import TokenObtainPairView

class GoogleLoginJWTSerializer(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:3000'
    
    def get_serializer(self, *args, **kwargs):
        return TokenObtainPairView.serializer_class(*args, **kwargs)
    
class FacebookLoginJWTSerializer(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:3000'
    
    

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/orders/", include("orders.urls")),
    path("api/products/", include("products.urls")),
    path("api/reports/", include("reports.urls")),
    path("api/transactions/", include("transactions.urls")),
    path("api/users/", include("users.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/shipping/", include("shipping.urls")),
    path("api/auth/", include('auth.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/google/', GoogleLoginJWTSerializer.as_view(), name='google_jwt'),
    path('api/auth/facebook/', FacebookLoginJWTSerializer.as_view(), name='facebook_jwt'),
    path('accounts/', include('allauth.urls')),
]
