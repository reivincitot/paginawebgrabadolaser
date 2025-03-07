from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User



class UpdatePhoneView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        user = self.get_objects()
        phone_number = request.data.get('phone_number')
        
        if User.objects.filter(phone_number=phone_number).exists():
            return Response({'phone_number': 'This phone number is already in use.'}, status=400)
        
        user.phone_number = phone_number
        user.save()
        return Response(self.get_serializer(user).data)