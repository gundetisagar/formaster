from formaster.interactors.storages.user_storage_interface import \
    UserStorageInterface
from formaster.exceptions.exceptions import (
    InvalidUsername,
    InvalidPassword,
    InvalidUserId,
    UserIsNotAdmin
)
from formaster.models.user import User
from formaster.dtos.dtos import UserDetailsDto


class UserStorageImplementation(UserStorageInterface):

    def validate_password(self, username: str, password: str) -> object:
        user_obj = User.objects.get(username=username)

        if not user_obj.check_password(password):
            raise InvalidPassword
        return user_obj


    def validate_username(self, username: str) -> bool:
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUsername
        return True

    def get_user_profile(self, user_id: int) -> UserDetailsDto:
        user = User.objects.get(id=user_id)
        user_details_dto = UserDetailsDto(
            user_id=user.id,
            username=user.username,
            is_admin=user.is_admin
        )
        return user_details_dto

    def validate_is_admin(self, user_id: int) -> bool:
        try:
            user = User.objects.get(id=user_id)
            print(user.is_admin)
        except User.DoesNotExist:
             raise InvalidUserId
        if user.is_admin == True:
            return True
        raise UserIsNotAdmin
