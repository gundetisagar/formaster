import pytest
from formaster.storages.user_storage_implementation import \
    UserStorageImplementation
from formaster.exceptions.exceptions import UserIsNotAdmin

@pytest.mark.django_db
def test_validate_is_admin_with_is_admin_true_returns_true(
        create_user):
    # arrnage
    user_id = 1
    user_storage = UserStorageImplementation()
    is_admin = True

    # Act
    return_value = user_storage.validate_is_admin(
        user_id=user_id
    )

    # Assert
    assert is_admin == return_value


@pytest.mark.django_db
def test_validate_is_admin_with_is_admin_false_raises_exception(
        create_second_user):
    # arrnage
    user_id = 1
    user_storage = UserStorageImplementation()
    

    # Act
    with pytest.raises(UserIsNotAdmin):
        user_storage.validate_is_admin(
            user_id=user_id
        )

    # # Assert
    # assert is_not_admin == return_value
