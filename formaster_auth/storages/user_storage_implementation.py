from formaster_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface
from formaster_auth.exceptions.exceptions import (
    InvalidUsername,
    InvalidPassword,
    InvalidUserId,
    UserIsNotAdmin,
    UserDoesNotExist
)
from formaster_auth.models.user import User
from formaster_auth.dtos.dtos import UserDetailsDto


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

    def validate_user_id(self, user_id: int) -> bool:
        try:
            User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise UserDoesNotExist
        return True

    def get_user_profile(self, user_id: int) -> UserDetailsDto:
        user_obj = User.objects.get(id=user_id)
        user_profile_dto = self._convert_user_obj_to_user_dto(user_obj)
        return user_profile_dto

    def validate_is_admin(self, user_id: int) -> bool:
        user = User.objects.get(id=user_id)

        if user.is_admin == True:
            return True
        raise UserIsNotAdmin

    def _convert_user_obj_to_user_dto(self, user_obj):
        user_profile_dto = UserDetailsDto(
            user_id=user_obj.id,
            username=user_obj.username,
            is_admin=user_obj.is_admin
        )
        return user_profile_dto