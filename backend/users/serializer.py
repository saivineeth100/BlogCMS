from pyexpat import model
from rest_framework import serializers

from users.models import User



    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ("is_active", "is_staff", "is_superuser", "date_joined","last_login")
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
        }
        fields = '__all__'

