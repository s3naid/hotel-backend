from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ["id", "display_name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

