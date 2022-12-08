from users.models import UserModel
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

# @brief ¿Qué consultas se van a poder hacer?
# @params ModelViewSet, 

class UserViewSet(viewsets.ModelViewSet):
  queryset = UserModel.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = UserSerializer