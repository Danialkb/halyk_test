from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class CreateTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    # password = serializers.CharField(max_length=128)
