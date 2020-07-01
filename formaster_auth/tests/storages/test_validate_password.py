import pytest
from formaster_auth.storages.user_storage_implementation import \
    UserStorageImplementation
# from django.core.exceptions import DoesNotExist
from formaster_auth.exceptions.exceptions import InvalidUsername, InvalidPassword
from formaster_auth.models.user import User


@pytest.mark.django_db
def test_validate_password_with_valid_password(create_user):
    # Arrange
    username = "username"
    password = "password"
    user_id = 1
    user_storage = UserStorageImplementation()

    # Act
    user_obj = user_storage.validate_password(
        username=username,
        password=password
    )

    # Assert
    expected_user_obj = User.objects.get(id=user_id)
    assert expected_user_obj == user_obj
    assert expected_user_obj.id == user_obj.id
    assert expected_user_obj.is_admin == user_obj.is_admin

@pytest.mark.django_db
def test_validate_password_with_invalid_password(create_user):
    # Arrange
    username = "username"
    password = "invalidpassword"
    user_storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidPassword):
        user_storage.validate_password(
            username=username,
            password=password
        )
