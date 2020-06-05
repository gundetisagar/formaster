from abc import abstractmethod

from formaster.dtos.dtos import UserDetailsDto


class UserStorageInterface:

    @abstractmethod
    def validate_username(self, username: str) -> bool:
        pass

    @abstractmethod
    def validate_password(self, username: str, password: str) -> object:
        pass

    @abstractmethod
    def get_user_profile(self, user_id: int) -> UserDetailsDto:
        pass

    @abstractmethod
    def validate_is_admin(self, user_id: int) -> bool:
        pass
