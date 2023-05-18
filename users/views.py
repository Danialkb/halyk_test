from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models, serializers
from .services import UserService, UserServiceV1


class UserViewSet(ModelViewSet):
    user_service: UserService = UserServiceV1()
    queryset = user_service.get_users()
    serializer_class = serializers.UserSerializer

    @action(detail=False, methods=['POST'])
    def create_token(self, request, *args, **kwargs):
        serializer = serializers.CreateTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tokens = self.user_service.create_token(data=serializer.data)

        return Response(tokens)



