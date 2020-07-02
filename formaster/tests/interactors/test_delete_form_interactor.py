import pytest
from unittest.mock import create_autospec, patch
from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.user_storage_interface import \
    UserStorageInterface
from formaster.interactors.delete_form_interactor import \
    DeleteFormInteractor
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from formaster_auth.exceptions.exceptions import UserDoesNotExist, \
        UserIsNotAdmin
from formaster.adapters.user_service import UserService
from formaster.exceptions.exceptions import FormDoesNotExist, \
        UserIsNotCreaterOfForm


@patch.object(UserService, "interface")
def test_delete_form_with_invalid_user_id_raises_exception(interface_mock):
    # Arrange
    user_id = 1
    form_id = 1
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interface_mock.validate_user_id.side_effect = UserDoesNotExist
    presenter.raise_exception_for_invalid_user_id.side_effect = NotFound

    interactor = DeleteFormInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.delete_form_wrapper(
            user_id=user_id,
            form_id=form_id,
            presenter=presenter
        )

    # Assert
    interface_mock.validate_user_id.assert_called_once_with(user_id)
    presenter.raise_exception_for_invalid_user_id.assert_called_once()


@patch.object(UserService, "interface")
def test_delete_form_with_valid_user_id_returns_true(interface_mock):
    # Arrange
    user_id = 1
    form_id = 1
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interface_mock.validate_user_id.return_value = True

    interactor = DeleteFormInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_form_wrapper(
        user_id=user_id,
        form_id=form_id,
        presenter=presenter
    )

    # Assert
    interface_mock.validate_user_id.assert_called_once_with(user_id)
    presenter.raise_exception_for_invalid_user_id.assert_not_called()


@patch.object(UserService, "interface")
def test_delete_form_with_user_is_not_admin(interface_mock):
    # Arrange
    user_id = 1
    form_id = 1
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interface_mock.validate_is_admin.side_effect = UserIsNotAdmin
    presenter.raise_exception_for_user_is_not_admin.side_effect = NotFound

    interactor = DeleteFormInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.delete_form_wrapper(
            user_id=user_id,
            form_id=form_id,
            presenter=presenter
        )

    # Assert
    interface_mock.validate_is_admin.assert_called_once_with(user_id)
    presenter.raise_exception_for_user_is_not_admin.assert_called_once()



@patch.object(UserService, "interface")
def test_delete_form_with_user_is_admin(interface_mock):
    # Arrange
    user_id = 1
    form_id = 1

    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interface_mock.validate_is_admin.return_value = True

    interactor = DeleteFormInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_form_wrapper(
        user_id=user_id,
        form_id=form_id,
        presenter=presenter
    )

    # Assert
    interface_mock.validate_is_admin.assert_called_once_with(user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()



@patch.object(UserService, "interface")
def test_delete_form_with_invalid_form_id_raises_exception(interface_mock):
    # Arrange
    user_id = 1
    invalid_form_id = 0
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)

    form_storage.validate_form_id.side_effect = FormDoesNotExist
    presenter.raise_exception_for_invalid_form_id.side_effect = NotFound

    interactor = DeleteFormInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.delete_form_wrapper(
            user_id=user_id,
            form_id=invalid_form_id,
            presenter=presenter
        )

    # Assert
    interface_mock.validate_user_id.assert_called_once_with(user_id)
    interface_mock.validate_is_admin.assert_called_once_with(user_id)
    form_storage.validate_form_id.assert_called_once_with(
        form_id=invalid_form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_called_once()


@patch.object(UserService, "interface")
def test_delete_form_with_valid_form_id_returns_true(interface_mock):
    # Arrange
    user_id = 1
    form_id = 1
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)

    form_storage.validate_form_id.return_value = True

    interactor = DeleteFormInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_form_wrapper(
        user_id=user_id,
        form_id=form_id,
        presenter=presenter
    )

    # Assert
    form_storage.validate_form_id.assert_called_once_with(
        form_id=form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_not_called()

@patch.object(UserService, "interface")
def test_delete_form_with_user_not_creater_of_form_raise_exception(
        interface_mock):
    # Arrange
    user_id = 1
    form_id = 2
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)

    form_storage.validate_is_user_creater_of_form.side_effect = \
        UserIsNotCreaterOfForm
    presenter.raise_exception_for_user_is_not_creater_of_form.side_effect = \
        NotFound

    interactor = DeleteFormInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.delete_form_wrapper(
            user_id=user_id,
            form_id=form_id,
            presenter=presenter
        )

    # Assert
    form_storage.validate_is_user_creater_of_form.assert_called_once_with(
        user_id=user_id, form_id=form_id
    )
    presenter.raise_exception_for_user_is_not_creater_of_form. \
        assert_called_once()


@patch.object(UserService, "interface")
def test_delete_form_with_user_is_creater_of_form_returns_true(interface_mock):
    # Arrange
    user_id = 1
    form_id = 1
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)

    form_storage.validate_is_user_creater_of_form.return_value = True

    interactor = DeleteFormInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_form_wrapper(
        user_id=user_id,
        form_id=form_id,
        presenter=presenter
    )

    # Assert
    form_storage.validate_is_user_creater_of_form.assert_called_once_with(
        user_id=user_id, form_id=form_id
    )
    presenter.raise_exception_for_user_is_not_creater_of_form. \
        assert_not_called()

