import pytest
from unittest.mock import create_autospec
from formaster_auth.interactors.validate_user_id import \
	ValidateUserIdInteractor
from formaster_auth.interactors.storages.user_storage_interface import \
	UserStorageInterface
from formaster_auth.exceptions.exceptions import UserDoesNotExist


def test_validate_user_id_with_invalid_user_id_raises_exception():
	# Arrange
	user_id = 0
	user_storage = create_autospec(UserStorageInterface)
	interactor = ValidateUserIdInteractor(
		user_storage=user_storage
	)
	user_storage.validate_user_id.side_effect = UserDoesNotExist

	# Act
	with pytest.raises(UserDoesNotExist):
		interactor.validate_user_id(user_id)


def test_validate_user_id_with_valid_user_returns_true():
	# Arrange
	user_id = 1
	is_valid_user = True

	user_storage = create_autospec(UserStorageInterface)
	interactor = ValidateUserIdInteractor(
		user_storage=user_storage
	)
	user_storage.validate_user_id.return_value = True

	# Act
	return_value = interactor.validate_user_id(user_id)

	# Assert
	assert is_valid_user == return_value
