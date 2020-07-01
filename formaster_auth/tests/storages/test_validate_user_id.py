

import pytest
from formaster_auth.storages.user_storage_implementation import \
    UserStorageImplementation
from formaster_auth.exceptions.exceptions import UserDoesNotExist

@pytest.mark.django_db
def test_validate_user_id_valid_user_id_returns_true(
        create_user):
    # arrnage
    user_id = 1
    user_storage = UserStorageImplementation()
    valid_user_id = True

    # Act
    return_value = user_storage.validate_user_id(
        user_id=user_id
    )

    # Assert
    assert valid_user_id == return_value


@pytest.mark.django_db
def test_validate_user_id_invalid_user_id_returns_false(create_user):
    # arrnage
    user_id = 0
    user_storage = UserStorageImplementation()

    # Act
    with pytest.raises(UserDoesNotExist):
        user_storage.validate_user_id(user_id=user_id)
