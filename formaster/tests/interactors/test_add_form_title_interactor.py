from unittest.mock import create_autospec
import pytest
from formaster.interactors.add_form_title_interactor import \
    AddFormTitleInteractor
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.interactors.storages.user_storage_interface import \
    UserStorageInterface


def test_add_form_title_(form_title_with_id_dto):
    # Arrange
    user_id = 1
    form_title = "Snacks Form"
    form_storage = create_autospec(FormStorageInterface)
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    expected_form_details_dto = form_title_with_id_dto
    expected_form_title_with_id_dict = {
        "form_id": 1,
        "form_title": "new form title"
    }

    form_storage.add_form_title.return_value = expected_form_details_dto
    presenter.add_form_title_response.return_value = \
        expected_form_title_with_id_dict

    interactor = AddFormTitleInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    # Act
    form_title_with_id_dict = interactor.add_form_title(
        user_id=user_id,
        form_title=form_title
    )

    # Assert
    form_storage.add_form_title.assert_called_once_with(
        user_id=user_id,
        form_title=form_title
    )
    presenter.add_form_title_response.assert_called_once_with(
        form_title_with_id_dto
    )
    assert expected_form_title_with_id_dict == form_title_with_id_dict
