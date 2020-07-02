from unittest.mock import create_autospec, patch
import pytest
from formaster.interactors.add_form_title_interactor import \
    AddFormTitleInteractor
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.adapters.user_service import UserService
from formaster_auth.exceptions.exceptions import UserIsNotAdmin, UserDoesNotExist
from django_swagger_utils.drf_server.exceptions import Forbidden, NotFound


class TestAddFormTite:

    @staticmethod
    @patch.object(UserService, "interface")
    def test_with_invalid_user_id_raises_exception(interface_mock):
        # Arrange
        user_id = 0
        form_title = "Snacks Form"
        form_storage = create_autospec(FormStorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = AddFormTitleInteractor(
            form_storage=form_storage,
            presenter=presenter
        )

        interface_mock.validate_user_id.side_effect = UserDoesNotExist
        presenter.raise_exception_for_invalid_user_id.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.add_form_title_wrapper(
                user_id=user_id,
                form_title=form_title,
                presenter=presenter
            )

        # Assert
        interface_mock.validate_user_id.assert_called_once_with(user_id)
        presenter.raise_exception_for_invalid_user_id.assert_called_once()

    @staticmethod
    @patch.object(UserService, "interface")
    def test_with_valid_user_id_returns_true(interface_mock):
        # Arragne
        user_id = 1
        form_title = "Snacks Form"
        form_storage = create_autospec(FormStorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = AddFormTitleInteractor(
            form_storage=form_storage,
            presenter=presenter
        )

        interface_mock.validate_user_id.return_value = True

        # Act
        interactor.add_form_title_wrapper(
            user_id=user_id,
            form_title=form_title,
            presenter=presenter
        )

        # Assert
        interface_mock.validate_user_id.assert_called_once_with(user_id)
        presenter.raise_exception_for_invalid_user_id.assert_not_called()


    @staticmethod
    @patch.object(UserService, "interface")
    def test_with_user_is_not_admin_raises_exception(interface_mock):
        # Arrange
        user_id = 1
        form_title = "Snacks Form"
        form_storage = create_autospec(FormStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interface_mock.validate_is_admin.side_effect = UserIsNotAdmin
        presenter.raise_exception_for_user_is_not_admin.side_effect = Forbidden

        interactor = AddFormTitleInteractor(
            form_storage=form_storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(Forbidden):
            interactor.add_form_title_wrapper(
                user_id=user_id,
                form_title=form_title,
                presenter=presenter
            )

        # Assert
        interface_mock.validate_is_admin.assert_called_once_with(user_id)
        presenter.raise_exception_for_user_is_not_admin.assert_called_once()

    @staticmethod
    @patch.object(UserService, "interface")
    def test_with_admin_user_returns_true(interface_mock):
        # Arrange
        user_id = 1
        form_title = "Snacks Form"
        form_storage = create_autospec(FormStorageInterface)
        presenter = create_autospec(PresenterInterface)

        interface_mock.validate_is_admin.return_value = True

        interactor = AddFormTitleInteractor(
            form_storage=form_storage,
            presenter=presenter
        )

        # Act
        interactor.add_form_title_wrapper(
            user_id=user_id,
            form_title=form_title,
            presenter=presenter
        )

        # Assert
        interface_mock.validate_is_admin.assert_called_once_with(user_id)
        presenter.raise_exception_for_user_is_not_admin.assert_not_called()


    @staticmethod
    @patch.object(UserService, "interface")
    def test_with_all_valid_details_returns_form_details(
            interface_mock, form_details_dto):
        # Arrange
        user_id = 1
        form_title = "Snacks Form"
        form_storage = create_autospec(FormStorageInterface)
        presenter = create_autospec(PresenterInterface)
        expected_form_details_dto = form_details_dto
        expected_form_details_dict = {
            "form_id": 1,
            "form_title": "Snacks Form"
        }

        interface_mock.validate_user_id.return_value = True
        interface_mock.validate_is_admin.return_value = True
        form_storage.add_form_title.return_value = expected_form_details_dto
        presenter.add_form_title_response.return_value = \
            expected_form_details_dict


        interactor = AddFormTitleInteractor(
            form_storage=form_storage,
            presenter=presenter
        )

        # Act
        form_details_dict = interactor.add_form_title_wrapper(
            user_id=user_id,
            form_title=form_title,
            presenter=presenter
        )

        # Assert
        interface_mock.validate_user_id.assert_called_once_with(user_id)
        interface_mock.validate_is_admin.assert_called_once_with(user_id)
        form_storage.add_form_title.assert_called_once_with(
            user_id=user_id,
            form_title=form_title
        )
        presenter.add_form_title_response.assert_called_once_with(
            form_details_dto=expected_form_details_dto
        )
        assert expected_form_details_dict == form_details_dict
