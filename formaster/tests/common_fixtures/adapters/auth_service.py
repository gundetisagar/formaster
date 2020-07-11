from typing import List
import pytest

# from fb_post_clean_arch_v2.adapters.dtos import UserDTO

def invalid_is_admin_mock(mocker, user_id: int):
    from formaster_auth.exceptions.exceptions import UserIsNotAdmin
    mock = mocker.patch(
        'formaster.adapters.user_service.UserService.validate_is_admin'
    )
    mock.side_effect = UserIsNotAdmin
    return

def invalid_user_id_mock(mocker, user_id: int):
    from formaster_auth.exceptions.exceptions import UserDoesNotExist
    mock = mocker.patch(
        'formaster.adapters.user_service.UserService.validate_user_id'
    )
    mock.side_effect = UserDoesNotExist
    return

def is_valid_user_mock(mocker, user_id: int):
    mock = mocker.patch(
        'formaster.adapters.user_service.UserService.validate_user_id'
    )
    mock.return_value = True
    return

def is_valid_admin_mock(mocker, user_id: int):
    mock = mocker.patch(
        'formaster.adapters.user_service.UserService.validate_is_admin'
    )
    mock.return_value = True
    return




# def prepare_get_user_dtos_mock(mocker, user_ids: List[int]):
#     mock = mocker.patch(
#         'fb_post_clean_arch_v2.adapters.auth_service.AuthService.get_user_dtos'
#     )
#     user_dtos = [
#         UserDTO(
#             user_id=user_id,
#             name="user_{}".format(_index + 1),
#             profile_pic_url="profile_{}".format(_index + 1)
#         ) for _index, user_id in enumerate(user_ids)
#     ]
#     mock.return_value = user_dtos
#     return mock
# class UserService:
# 	@property
# 	def interface(self):
# 		from formaster_auth.interfaces.user_interface import UserInterface
# 		return UserInterface()

# 	def validate_user_id(self, user_id: int):
# 		is_valid_user = self.interface.validate_user_id(user_id)
# 		return is_valid_user

# 	def validate_is_admin(self, user_id: int):
# 		is_user_admin = self.interface.validate_is_admin(user_id)
# 		return is_user_admin
