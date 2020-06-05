import pytest
from formaster.storages.question_storage_implementation import \
    QuestionStorageImplementation
from formaster.constants.enums import QuestionTypes


@pytest.mark.django_db
def test_questions_create_with_text_create_question(
        create_user, create_two_form_titles):

    # Arrange
    form_id = 1
    question_type = QuestionTypes.LARGE_TEXT.value
    question_text = "log in"
    required = False
    description = ""
    question_id = 1
    question_storage = QuestionStorageImplementation()

    # Act
    returns_question_id = question_storage.create_text_question(
        form_id=form_id,
        question_type=question_type,
        question_text=question_text,
        required=required,
        description=description)

    # Assert
    assert question_id == returns_question_id

@pytest.mark.django_db
def test_questions_create_with_mcq_create_question(
        create_user, create_two_form_titles):

    # Arrange
    form_id = 1
    question_type = QuestionTypes.MCQ.value
    question_text = "log in"
    required = False
    description = ""
    choices_list = ["A", "B", "C"]
    expected_question_id = 1
    question_storage = QuestionStorageImplementation()
    question_id = question_storage.create_text_question(
        form_id=form_id,
        question_type=question_type,
        question_text=question_text,
        required=required,
        description=description)

    # Act
    question_storage.create_mcq_choices(
        question_id=question_id,
        choices_list=choices_list
    )

    # Assert
    assert expected_question_id == question_id
