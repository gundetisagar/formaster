import pytest
from unittest.mock import create_autospec, patch
from mixin_formaster.interactors.storages.storage_interface import \
    StorageInterface
from mixin_formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from mixin_formaster.interactors.form_questions_interactor import \
    GetFormQuestionsInteractor
from mixin_formaster.dtos.dtos import FormQuestionsDetailsDTO
from mixin_formaster.exceptions.exceptions import FormDoesNotExist


def test_get_form_questions_interactor(form_details_dto, questions_details_dto,
                                       choice_details_dto):
    # Arrange
    form_id = 1
    question_ids = [1,2]
    mcq_question_ids = [1, 2]

    form_questions_details = FormQuestionsDetailsDTO(
        form_details=form_details_dto,
        questions_details=questions_details_dto,
        choice_details=choice_details_dto
    )
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetFormQuestionsInteractor(
        form_id, storage
    )

    storage.get_form_details.return_value = form_details_dto
    storage.get_question_ids.return_value = question_ids
    storage.get_mcq_question_ids.return_value = mcq_question_ids
    storage.get_choice_details.return_value = choice_details_dto
    storage.get_questions_details.return_value = questions_details_dto

    # Act
    returns_form_questions_details_dto = interactor.get_form_questions_wrapper(
        presenter=presenter
    )

    # Assert
    storage.get_form_details.assert_called_once_with(form_id)
    storage.get_question_ids.assert_called_once_with(form_id)
    storage.get_mcq_question_ids.assert_called_once_with(question_ids)
    storage.get_choice_details.assert_called_once_with(mcq_question_ids)
    storage.get_questions_details.assert_called_once_with(question_ids)


def test_get_form_questions_with_invalid_form_id():
    # Arrnage
    from django_swagger_utils.drf_server.exceptions import NotFound
    form_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetFormQuestionsInteractor(
        form_id, storage
    )

    storage.is_valid_form_id.side_effect = FormDoesNotExist
    presenter.raise_form_does_not_exist_exception.side_effect = NotFound

    # Act

    with pytest.raises(NotFound):
        interactor.get_form_questions_wrapper(presenter=presenter)
    # Assert
    storage.is_valid_form_id.assert_called_once_with(form_id)
    presenter.raise_form_does_not_exist_exception.assert_called_once()

#---------------------UserGetQuestionsInteractor tests----------------------->

from mixin_formaster.interactors.user_get_questions import \
    UserGetQuestionsInteractor

# def test_user_get_questions_with_invalid_form_id():
#     # Arrnage
#     from django_swagger_utils.drf_server.exceptions import NotFound
#     form_id = 1

#     storage = create_autospec(StorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = UserGetQuestionsInteractor(
#         storage
#     )

#     storage.is_valid_form_id.side_effect = FormDoesNotExist
#     presenter.raise_form_does_not_exist_exception.side_effect = NotFound

#     # Act

#     with pytest.raises(NotFound):
#         interactor.get_form_questions_wrapper(presenter=presenter)
#     # Assert
#     storage.is_valid_form_id.assert_called_once_with(form_id)
#     presenter.raise_form_does_not_exist_exception.assert_called_once()



@patch.object(GetFormQuestionsInteractor, "get_form_questions")
def test_user_get_questions_interactor(
        get_form_questions_mock,
        form_details_dto, questions_details_dto,
        choice_details_dto,
        response_details_dto,
        form_questions_and_response_details_dto):
    # Arrange
    user_id = 1
    form_id = 1
    question_ids = [1, 2]

    form_questions_details_dto = FormQuestionsDetailsDTO(
        form_details=form_details_dto,
        questions_details=questions_details_dto,
        choice_details=choice_details_dto
    )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UserGetQuestionsInteractor(storage=storage)

    get_form_questions_mock.return_value = form_questions_details_dto
    storage.get_response_details.return_value = response_details_dto

    # Act
    user_get_questions_details =  interactor.user_get_questions_wrapper(
        user_id, form_id, presenter
    )

    # Assert
    storage.get_response_details.assert_called_once_with(question_ids)
    presenter.user_get_questions_response(form_questions_and_response_details_dto)
