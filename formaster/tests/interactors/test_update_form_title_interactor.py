import pytest
from unittest.mock import create_autospec
from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.user_storage_interface import \
    UserStorageInterface
from formaster.interactors.update_form_title_interactor import \
    UpdateFormTitleInteractor
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from formaster.exceptions.exceptions import (
    UserIsNotCreaterOfForm,
    InvalidFormId,
    UserIsNotAdmin
)


def test_update_form_title_with_user_is_not_admin():
    # Arrange
    user_id = 1
    form_id = 1
    new_form_title = "new form title"
    form_storage = create_autospec(FormStorageInterface)
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.validate_is_admin.side_effect = UserIsNotAdmin

    interactor = UpdateFormTitleInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    # Act
    interactor.update_form_title(
        user_id=user_id,
        form_id=form_id,
        new_form_title=new_form_title
    )

    # Assert
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_called_once()
    form_storage.validate_form_id.assert_not_called()
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    form_storage.validate_is_user_creater_of_form.assert_not_called()
    presenter.raise_exception_for_user_cannot_update_form.assert_not_called()
    form_storage.update_form_title.assert_not_called()



def test_update_form_title_with_user_is_admin():
    # Arrange
    user_id = 1
    form_id = 1
    new_form_title = "New form title"
    form_storage = create_autospec(FormStorageInterface)
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.validate_is_admin.return_value = True
    form_storage.validate_form_id.return_value = True
    

    interactor = UpdateFormTitleInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    # Act
    interactor.update_form_title(
        user_id=user_id,
        form_id=form_id,
        new_form_title=new_form_title
    )

    # Assert
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(form_id=form_id)
    presenter.raise_exception_for_invalid_form_id.assert_not_called()


def test_update_form_title_with_invalid_form_id():
    # Arrange
    user_id = 1
    invalid_form_id = 0
    new_form_title = "new form title"
    form_storage = create_autospec(FormStorageInterface)
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.validate_is_admin.return_value = True
    form_storage.validate_form_id.side_effect = InvalidFormId

    interactor = UpdateFormTitleInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    # Act
    interactor.update_form_title(
        user_id=user_id,
        form_id=invalid_form_id,
        new_form_title=new_form_title
    )

    # Assert
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(
        form_id=invalid_form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_called_once()
    form_storage.validate_is_user_creater_of_form.assert_not_called()
    presenter.raise_exception_for_user_cannot_update_form.assert_not_called()
    form_storage.delete_form.assert_not_called()


def test_update_form_title_with_valid_form_id():
    # Arrange
    user_id = 1
    form_id = 1
    new_form_title = "new form title"
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_storage = create_autospec(UserStorageInterface)

    user_storage.validate_is_admin.return_value = True
    form_storage.validate_form_id.return_value = True


    interactor = UpdateFormTitleInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    # Act
    interactor.update_form_title(
        user_id=user_id,
        form_id=form_id,
        new_form_title=new_form_title
    )

    # Assert
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(
        form_id=form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    form_storage.validate_is_user_creater_of_form.assert_called_once_with(
        user_id=user_id, form_id=form_id
    )
    presenter.raise_exception_for_user_cannot_delete_form.assert_not_called()


def test_update_form_title_with_user_not_creater_of_form():
    # Arrange
    user_id = 1
    form_id = 2
    new_form_title = "new form title"
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_storage = create_autospec(UserStorageInterface)

    user_storage.validate_is_admin.return_value = True
    form_storage.validate_form_id.return_value = True
    form_storage.validate_is_user_creater_of_form.side_effect = \
        UserIsNotCreaterOfForm


    interactor = UpdateFormTitleInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    # Act
    interactor.update_form_title(
        user_id=user_id,
        form_id=form_id,
        new_form_title=new_form_title
    )

    # Assert
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(
        form_id=form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    form_storage.validate_is_user_creater_of_form.assert_called_once_with(
        user_id=user_id, form_id=form_id
    )
    presenter.raise_exception_for_user_cannot_update_form.assert_called_once()
    form_storage.delete_form.assert_not_called()


def test_update_form_title_with_user_is_creater_of_form():
    # Arrange
    user_id = 1
    form_id = 1
    new_form_title = "new form title"
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_storage = create_autospec(UserStorageInterface)

    user_storage.validate_is_admin.return_value = True
    form_storage.validate_form_id.return_value = True
    form_storage.validate_is_user_creater_of_form.return_value = True

    interactor = UpdateFormTitleInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    # Act
    interactor.update_form_title(
        user_id=user_id,
        form_id=form_id,
        new_form_title=new_form_title
    )

    # Assert
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(
        form_id=form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    form_storage.validate_is_user_creater_of_form.assert_called_once_with(
        user_id=user_id, form_id=form_id
    )
    presenter.raise_exception_for_user_cannot_delete_form.assert_not_called()


def test_update_form_title_with_all_valid_details(
        form_title_with_id_dto):
    # Arrange
    user_id = 1
    form_id = 1
    new_form_title = "new form title"
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_storage = create_autospec(UserStorageInterface)
    expected_form_title_with_id_dto = form_title_with_id_dto
    expected_form_title_with_id_dict = {
        "form_id": 1,
        "form_title": "new form title"
    }

    user_storage.validate_is_admin.return_value = True
    form_storage.validate_form_id.return_value = True
    form_storage.validate_is_user_creater_of_form.return_value = True
    form_storage.update_form_title.return_value = \
        expected_form_title_with_id_dto
    presenter.update_form_title_response.return_value = \
        expected_form_title_with_id_dict

    interactor = UpdateFormTitleInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    # Act
    form_title_with_id_dict = interactor.update_form_title(
        user_id=user_id,
        form_id=form_id,
        new_form_title=new_form_title
    )

    # Assert
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(
        form_id=form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    form_storage.validate_is_user_creater_of_form.assert_called_once_with(
        user_id=user_id, form_id=form_id
    )
    presenter.raise_exception_for_user_cannot_delete_form.assert_not_called()
    form_storage.update_form_title.assert_called_once_with(
        form_id=form_id,
        new_form_title=new_form_title
    )
    presenter.update_form_title_response.assert_called_once_with(
        form_title_with_id_dto=expected_form_title_with_id_dto
    )
    assert expected_form_title_with_id_dict == form_title_with_id_dict
