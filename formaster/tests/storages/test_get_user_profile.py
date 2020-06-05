import pytest
from formaster.storages.user_storage_implementation import \
    UserStorageImplementation
from formaster.dtos.dtos import UserDetailsDto

@pytest.mark.django_db
def test_get_user_profile(create_user):
    # Arrange
    user_id = 1
    user_storage = UserStorageImplementation()
    expected_user_profile_dto = UserDetailsDto(
        user_id=1,
        username="username",
        is_admin=True
    )

    user_profile_dto = user_storage.get_user_profile(
        user_id=user_id
    )

    # Assert
    assert expected_user_profile_dto == user_profile_dto
