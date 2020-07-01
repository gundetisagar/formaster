from unittest.mock import create_autospec
import pytest
from formaster_auth.interactors.get_user_profile_interactor import \
    GetUserProfileInteractor
from formaster_auth.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound
from formaster_auth.exceptions.exceptions import UserDoesNotExist


class TestGetUserProfile:

    @staticmethod
    def test_with_invalid_user_id_raises_exception():
        # Arragne
        invalid_user_id = 0
        user_storage_mock = create_autospec(UserStorageInterface)
        presenter_mock = create_autospec(PresenterInterface)

        user_storage_mock.validate_user_id.side_effect = UserDoesNotExist
        presenter_mock.raise_exception_for_user_does_not_exist.side_effect = \
            NotFound

        interactor = GetUserProfileInteractor(
            user_storage=user_storage_mock,
            presenter=presenter_mock
        )

        # Act
        with pytest.raises(NotFound):
            interactor.get_user_profile_wrapper(
                user_id=invalid_user_id,
                presenter=presenter_mock
            )

        # Assert
        user_storage_mock.validate_user_id.assert_called_once_with(
            invalid_user_id
        )
        presenter_mock.raise_exception_for_user_does_not_exist. \
            assert_called_once()


    @staticmethod
    def test_with_valid_user_id_return_user_details(user_profile_dtos):
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

        user_storage.validate_user_id.return_value = True
        user_storage.get_user_profile.return_value = expected_user_profile_dto
        presenter.get_user_profile_response.return_value = expected_dict

        interactor = GetUserProfileInteractor(
            user_storage=user_storage,
            presenter=presenter
        )

        # Act
        user_profile_dict = interactor.get_user_profile_wrapper(
            user_id=user_id,
            presenter=presenter
        )

        # Assert
        user_storage.validate_user_id.assert_called_once_with(user_id)
        presenter.raise_exception_for_user_does_not_exist.assert_not_called()
        user_storage.get_user_profile.assert_called_once_with(user_id)
        presenter.get_user_profile_response.assert_called_once_with(
            user_profile_dto=expected_user_profile_dto)
        assert expected_dict == user_profile_dict
