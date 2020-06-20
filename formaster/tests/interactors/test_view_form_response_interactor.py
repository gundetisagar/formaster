from unittest.mock import create_autospec, patch
import pytest
from formaster.interactors.view_form_response_interactor import \
    ViewFormResponseInteractor
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.interactors.storages.question_storage_interface import \
    QuestionStorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound
#from formaster.tests.interactors.conftest import view_form_response_dto


def test_view_form_response_with_invalid_form_id():
    # Arrange
    invalid_form_id = 0
    presenter = create_autospec(PresenterInterface)
    form_storage = create_autospec(FormStorageInterface)
    question_storage = create_autospec(QuestionStorageInterface)

    form_storage.validate_form_id.side_effect = NotFound

    interactor = ViewFormResponseInteractor(
        question_storage=question_storage,
        form_storage=form_storage,
        presenter=presenter
    )

    # Act
    interactor.get_form_view(form_id=invalid_form_id)

    # Assert
    form_storage.validate_form_id.assert_called_once_with(
        form_id=invalid_form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_called_once()
    question_storage.get_form_view.assert_not_called()
    presenter.get_form_view_response.assert_not_called()


# def test_view_form_response_with_valid_form_id(
#         view_form_response_dto, view_from_response_dict):
#     # Arrange
#     form_id = 1
#     presenter = create_autospec(PresenterInterface)
#     form_storage = create_autospec(FormStorageInterface)
#     question_storage = create_autospec(QuestionStorageInterface)
#     expected_view_form_response_dto = view_form_response_dto
#     expected_view_form_response_dict = view_from_response_dict

#     form_storage.validate_form_id.return_value = True
#     question_storage.get_form_view.return_value = \
#         expected_view_form_response_dto
#     presenter.get_form_view_response.return_value = \
#         expected_view_form_response_dict

#     interactor = ViewFormResponseInteractor(
#         question_storage=question_storage,
#         form_storage=form_storage,
#         presenter=presenter
#     )

#     # Act
#     return_view_form_response_dict = interactor.get_form_view(form_id=form_id)

#     # Assert
#     form_storage.validate_form_id.assert_called_once_with(form_id=form_id)
#     presenter.raise_exception_for_invalid_form_id.assert_not_called()
#     question_storage.get_form_view.assert_called_once_with(
#         form_id=form_id
#     )
#     assert expected_view_form_response_dict == return_view_form_response_dict
#     presenter.get_form_view_response.assert_called_once_with(
#         list_of_view_form_response_dto=expected_view_form_response_dto
#     )
