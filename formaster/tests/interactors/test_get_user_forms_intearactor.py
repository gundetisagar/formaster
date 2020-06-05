from unittest.mock import create_autospec
import pytest
from formaster.interactors.get_forms_interactor import \
    GetFormsInteractor
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface



def test_get_user_forms(form_title_with_id_two_dtos):
    # Arrange
    user_id = 1
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)
    expected_forms_dto = form_title_with_id_two_dtos
    expected_forms_list = [
        {
            "form_id": 1,
            "form_title": "Snacks form"
        },
        {
            "form_id": 2,
            "form_title": "Food form"
        }
    ]


    form_storage.get_forms.return_value = expected_forms_dto
    presenter.get_forms_response.return_value = expected_forms_list

    interactor = GetFormsInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    # Act
    list_of_form_titles_with_id = interactor.get_forms(
        user_id=user_id
    )

    # Assert
    form_storage.get_forms.assert_called_once_with(user_id=user_id)
    presenter.get_forms_response.assert_called_once_with(
        expected_forms_dto
    )
    assert expected_forms_list == list_of_form_titles_with_id
