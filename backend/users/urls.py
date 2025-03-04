from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    RegisterClientView,
    RegisterEmployeeView,
    ProfileView
    )


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin',include(router.urls)),
    path('register/client/', RegisterClientView.as_view(), name='register-client'),
    path('register/employee/', RegisterEmployeeView.as_view(), name='register-employee'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
]
