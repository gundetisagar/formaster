import pytest
from unittest.mock import create_autospec
from formaster_auth.interactors.storages.user_storage_interface import \
	UserStorageInterface
from formaster_auth.interactors.validate_is_admin import \
	ValidateIsAdminInteractor
from formaster_auth.exceptions.exceptions import InvalidUserId, UserIsNotAdmin

def test_validate_is_admin_with_invalid_user():
	#Arrange
	user_id = 0
	user_storage = create_autospec(UserStorageInterface)
	interactor = ValidateIsAdminInteractor(
		user_storage=user_storage
	)
	user_storage.validate_is_admin.side_effect = InvalidUserId

	#Act
	with pytest.raises(InvalidUserId):
		interactor.validate_is_admin(user_id)



def test_validate_is_admin_with_user_exists_but_not_admin():
	#Arrange
	user_id = 1
	user_storage = create_autospec(UserStorageInterface)
	interactor = ValidateIsAdminInteractor(
		user_storage=user_storage
	)
	user_storage.validate_is_admin.side_effect = UserIsNotAdmin

	#Act
	with pytest.raises(UserIsNotAdmin):
		interactor.validate_is_admin(user_id)


def test_validate_is_admin_with_valid_details():
	# Arrange
	user_id = 1
	user_storage = create_autospec(UserStorageInterface)
	interactor = ValidateIsAdminInteractor(
		user_storage=user_storage
	)
	expected_return_value = True
	user_storage.validate_is_admin.return_value = True

	# Act
	is_valid_admin = interactor.validate_is_admin(user_id)

	# Assert
	user_storage.validate_is_admin.assert_called_once_with(user_id)
	assert expected_return_value == is_valid_admin