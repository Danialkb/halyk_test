from typing import Protocol, OrderedDict

from rest_framework.generics import get_object_or_404

from users.models import User


class UserRepo(Protocol):

    @staticmethod
    def get_users() -> [User]: ...

    @staticmethod
    def get_user(data: OrderedDict) -> User: ...


class UserRepoV1:

    @staticmethod
    def get_users() -> [User]:
        return User.objects.all()

    @staticmethod
    def get_user(data: OrderedDict) -> User:
        return get_object_or_404(User, **data)
