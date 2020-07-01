from typing import List
from abc import abstractmethod
from formaster_auth.dtos.dtos import (
    UserAuthTokensDto,
    UserDetailsDto
)

class PresenterInterface():

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def user_login_response(self,
                            tokens_dto: UserAuthTokensDto,
                            is_admin: bool):
        pass

    @abstractmethod
    def get_user_profile_response(self, user_profile_dto: UserDetailsDto):
        pass

    @abstractmethod
    def raise_exception_for_is_not_admin(self):
        pass

    @abstractmethod
    def raise_exception_for_user_does_not_exist(self):
        pass
