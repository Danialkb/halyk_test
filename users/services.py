from typing import Protocol, OrderedDict

from rest_framework_simplejwt import tokens

from users.models import User
from users.repos import UserRepo, UserRepoV1


class UserService(Protocol):

    def get_users(self) -> [User]: ...

    def create_token(self, data: OrderedDict) -> dict: ...


class UserServiceV1:
    user_repo: UserRepo = UserRepoV1()

    def get_users(self) -> [User]:
        return self.user_repo.get_users()

    def create_token(self, data: OrderedDict) -> dict:
        user = self.user_repo.get_user(data=data)

        if not user:
            return {"detail": 'Invalid username or password'}

        access = tokens.AccessToken.for_user(user)
        refresh = tokens.RefreshToken.for_user(user)

        return {
            'access': str(access),
            'refresh': str(refresh),
        }



