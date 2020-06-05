from unittest.mock import create_autospec
from formaster.interactors.questions_create_interactor import \
    QuestionsCreateInteractor
from formaster.interactors.storages.question_storage_interface import \
    QuestionStorageInterface
from formaster.constants.enums import QuestionTypes


def test_questions_create_with_text_question():
    # Arrange
    form_id = 1
    question_type = QuestionTypes.SMALL_TEXT.value
    question_text = "what is your name?"
    required = True
    description = "arrangement for food"
    questions_list = [{
        "question_type": QuestionTypes.SMALL_TEXT.value,
        "question_text": "what is your name?",
        "required": True,
        "description": "arrangement for food",
        "choices_list": []
    }]
    question_id = 1

    question_storage = create_autospec(QuestionStorageInterface)

    question_storage.create_text_question.return_value = question_id

    interactor = QuestionsCreateInteractor(question_storage=question_storage)

    # Act
    interactor.questions_create(
        form_id=form_id,
        questions_list=questions_list
    )

    # Assert
    question_storage.create_text_question.assert_called_once_with(
        form_id=form_id,
        question_type=question_type,
        question_text=question_text,
        required=required,
        description=description
    )
    question_storage.create_mcq_choices.assert_not_called()


def test_questions_create_with_mcq_question():
    form_id = 1
    question_type = QuestionTypes.MCQ.value
    question_text = "what is your name?"
    required = True
    description = "arrangement for food"
    choices_list = ["A", "B", "C"]
    questions_list = [{
        "question_type": QuestionTypes.MCQ.value,
        "question_text": "what is your name?",
        "required": True,
        "description": "arrangement for food",
        "choices_list": ["A", "B", "C"]
    }]
    question_id = 1

    question_storage = create_autospec(QuestionStorageInterface)

    question_storage.create_text_question.return_value = question_id

    interactor = QuestionsCreateInteractor(question_storage=question_storage)

    # Act
    interactor.questions_create(
        form_id=form_id,
        questions_list=questions_list
    )

    # Assert
    question_storage.create_text_question.assert_called_once_with(
        form_id=form_id,
        question_type=question_type,
        question_text=question_text,
        required=required,
        description=description
    )
    question_storage.create_mcq_choices.assert_called_once_with(
        question_id=question_id,
        choices_list=choices_list
    )
