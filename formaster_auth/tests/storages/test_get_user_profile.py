import pytest
from formaster_auth.storages.user_storage_implementation import \
    UserStorageImplementation
from formaster_auth.dtos.dtos import UserDetailsDto


class TestGetUserProfile:

    @staticmethod
    @pytest.mark.django_db
    def test_get_user_profile(create_user, snapshot):
        # Arrange
        user_id = 1
        user_storage = UserStorageImplementation()

        # Act
        user_profile_dto = user_storage.get_user_profile(
            user_id=user_id
        )

        # Assert
        snapshot.assert_match(user_profile_dto, "user_profile_dto")
