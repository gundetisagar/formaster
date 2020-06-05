import pytest
from formaster.storages.user_storage_implementation import \
    UserStorageImplementation
# from django.core.exceptions import DoesNotExist
from formaster.exceptions.exceptions import InvalidUsername, InvalidPassword
from formaster.models import User



@pytest.mark.django_db
def test_validate_username_with_valid_username(create_user):
    # Arrange
    username = "username"
    user_storage = UserStorageImplementation()
    valid_username = True

    # Act
    user_validation = user_storage.validate_username(username=username)

    # Assert
    assert valid_username == user_validation


@pytest.mark.django_db
def test_validate_username_with_invalid_username(create_user):
    # Arrange
    invalid_username = "invalidusername"
    user_storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidUsername):
        user_storage.validate_username(username=invalid_username)
