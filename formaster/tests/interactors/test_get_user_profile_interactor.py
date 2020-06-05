from unittest.mock import create_autospec
import pytest
from formaster.interactors.get_user_profile_interactor import \
    GetUserProfileInteractor
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.user_storage_interface import \
    UserStorageInterface


def test_get_user_profile(user_profile_dtos):
    # Arrange
    user_id = 1
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    expected_user_profile_dto = user_profile_dtos
    expected_dict = {
        "user_id": 1,
        "username": "user",
        "is_admin": True
    }

    user_storage.get_user_profile.return_value = expected_user_profile_dto
    presenter.get_user_profile_response.return_value = expected_dict

    interactor = GetUserProfileInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    # Act
    user_profile_dict = interactor.get_user_profile(
        user_id=user_id
    )

    # Assert
    assert expected_dict == user_profile_dict
    user_storage.get_user_profile.assert_called_once_with(user_id=user_id)
    presenter.get_user_profile_response.assert_called_once_with(
        user_profile_dto=expected_user_profile_dto)
