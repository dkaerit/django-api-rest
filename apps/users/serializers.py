from rest_framework import serializers
from .models import UserModel

# @brief convertir un modelo en datos que podrán ser consultados
# @params ModelSerializers, 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'password')
        #read_only_fields = ('')