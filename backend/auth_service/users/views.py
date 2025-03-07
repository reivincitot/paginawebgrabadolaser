from rest_framework import generics, permissions, viewsets
from .models import User
from .serializers import UserSerializer, ClientSerializer, EmployeeSerializer

class RegisterClientView(generics.CreateAPIView):
    """Public register for clients"""
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]

class RegisterEmployeeView(generics.CreateAPIView):
    """Public register for employees"""
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]
    
class ProfileView(generics.RetrieveUpdateAPIView):
    """Profile view for authenticated users"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
class UserAdminView(generics.ListCreateAPIView):
    """Admin view for users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    
class UserViewSet(viewsets.ModelViewSet):
    """View set for users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    