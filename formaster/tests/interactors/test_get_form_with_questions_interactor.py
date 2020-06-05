from unittest.mock import create_autospec
import pytest
from formaster.interactors.get_form_with_questions_interactor import \
    GetFormWithQuestionsInteractor
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.question_storage_interface import \
    QuestionStorageInterface



def test_get_form_with_questions(list_of_questions_dtos,
                                 list_of_questions_dict):
    # Arrange
    form_id = 1
    question_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    expected_list_of_questions_dto = list_of_questions_dtos
    expected_list_of_questions_dict = list_of_questions_dict

    question_storage.get_form_with_questions.return_value = \
        expected_list_of_questions_dto
    presenter.get_form_with_questions_response.return_value = \
        expected_list_of_questions_dict

    interactor = GetFormWithQuestionsInteractor(
        question_storage=question_storage,
        presenter=presenter
    )

    # Act
    returns_list_of_questions_dict = interactor.get_form_with_questions(
        form_id=form_id
    )


    # Assert
    assert expected_list_of_questions_dict == returns_list_of_questions_dict
    question_storage.get_form_with_questions.assert_called_once_with(
        form_id=form_id
    )
    presenter.get_form_with_questions_response.assert_called_once_with(
        list_of_questions_dtos
    )
