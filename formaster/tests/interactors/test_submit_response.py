from unittest.mock import create_autospec
import pytest
from formaster.interactors.submit_response_interactor import \
    SubmitResponseInteractor
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.response_storage_interface import \
    ResponseStorageInterface
from formaster.interactors.storages.choice_storage_interface import \
    ChoiceStorageInterface
from formaster.interactors.storages.question_storage_interface import \
    QuestionStorageInterface
from formaster.exceptions.exceptions import (
    InvalidQuestionId,
    InvalidChoiceId
)



def test_submit_response_with_responese_text_is_none():
    # Arrange
    user_id = 1
    question_id = 1
    response_text = None
    choice_id = 1
    response_list = [
        {
            "question_id": 1,
            "response_text": None,
            "choice_id": 1
        }
    ]

    questions_storage = create_autospec(QuestionStorageInterface)
    response_storage = create_autospec(ResponseStorageInterface)
    choice_storage = create_autospec(ChoiceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    questions_storage.validate_question_id.return_value = True
    choice_storage.validate_choice_id.return_value = True

    interactor = SubmitResponseInteractor(
        response_storage=response_storage,
        questions_storage=questions_storage,
        choice_storage=choice_storage,
        presenter=presenter
    )

    # Act
    interactor.submit_response(
        user_id=user_id,
        response_list=response_list
    )

    # Assert
    response_storage.submit_response.assert_called_with(
        user_id=user_id,
        question_id=question_id,
        response_text=response_text,
        choice_id=choice_id
    )
    questions_storage.validate_question_id.assert_called_with(
        question_id=question_id
    )
    choice_storage.validate_choice_id.assert_called_with(
        choice_id=choice_id
    )
    presenter.raise_exception_for_invalid_question_id.assert_not_called()
    presenter.raise_exception_for_invalid_choice_id.assert_not_called()


def test_submit_response_with_choice_id_is_none():
    # Arrange
    user_id = 1
    question_id = 1
    response_text = "answer_1"
    choice_id = None
    response_list = [
        {
            "question_id": 1,
            "response_text": "answer_1",
            "choice_id": None
        }
    ]

    questions_storage = create_autospec(QuestionStorageInterface)
    response_storage = create_autospec(ResponseStorageInterface)
    choice_storage = create_autospec(ChoiceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    questions_storage.validate_question_id.return_value = True
    choice_storage.validate_choice_id.return_value = True

    interactor = SubmitResponseInteractor(
        response_storage=response_storage,
        questions_storage=questions_storage,
        choice_storage=choice_storage,
        presenter=presenter
    )

    # Act
    interactor.submit_response(
        user_id=user_id,
        response_list=response_list
    )

    # Assert
    response_storage.submit_response.assert_called_with(
        user_id=user_id,
        question_id=question_id,
        response_text=response_text,
        choice_id=choice_id
    )
    questions_storage.validate_question_id.assert_called_with(
        question_id=question_id
    )
    choice_storage.validate_choice_id.assert_called_with(
        choice_id=choice_id
    )
    presenter.raise_exception_for_invalid_question_id.assert_not_called()
    presenter.raise_exception_for_invalid_choice_id.assert_not_called()



def test_submit_response_with_invalid_question_id_and_raise_exception():
    # Arrange
    user_id = 1
    invalid_question_id = 0
    response_list = [
        {
            "question_id": 0,
            "response_text": None,
            "choice_id": None
        }
    ]
    
    questions_storage = create_autospec(QuestionStorageInterface)
    response_storage = create_autospec(ResponseStorageInterface)
    choice_storage = create_autospec(ChoiceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    questions_storage.validate_question_id.side_effect = InvalidQuestionId
    #choice_storage.validate_choice_id.return_value = False

    interactor = SubmitResponseInteractor(
        response_storage=response_storage,
        questions_storage=questions_storage,
        choice_storage=choice_storage,
        presenter=presenter
    )

    # Act
    interactor.submit_response(
        user_id=user_id,
        response_list=response_list
    )

    # Assert
    #response_storage.submit_response.assert_not_called()
    questions_storage.validate_question_id.assert_called_with(
        question_id=invalid_question_id
    )
    presenter.raise_exception_for_invalid_question_id.assert_called_once()
    choice_storage.validate_choice_id.assert_not_called()
    presenter.raise_exception_for_invalid_choice_id.assert_not_called()
    response_storage.submit_response.assert_not_called()


def test_submit_response_with_invalid_choice_id_and_raise_exception():
    # Arrange
    user_id = 1
    question_id = 1
    invalid_choice_id = 0
    response_list = [
        {
            "question_id": 1,
            "response_text": None,
            "choice_id": 0
        }
    ]
    
    questions_storage = create_autospec(QuestionStorageInterface)
    response_storage = create_autospec(ResponseStorageInterface)
    choice_storage = create_autospec(ChoiceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    questions_storage.validate_question_id.return_value = True
    choice_storage.validate_choice_id.side_effect = InvalidChoiceId

    interactor = SubmitResponseInteractor(
        response_storage=response_storage,
        questions_storage=questions_storage,
        choice_storage=choice_storage,
        presenter=presenter
    )

    # Act
    interactor.submit_response(
        user_id=user_id,
        response_list=response_list
    )

    # Assert
    questions_storage.validate_question_id.assert_called_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question_id.assert_not_called()
    choice_storage.validate_choice_id.assert_called_once_with(
        choice_id=invalid_choice_id
    )
    presenter.raise_exception_for_invalid_choice_id.assert_called_once()
    response_storage.submit_response.assert_not_called()
