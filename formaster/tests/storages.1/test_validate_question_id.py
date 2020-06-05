import pytest
from formaster.storages.question_storage_implementation import \
    QuestionStorageImplementation
from formaster.exceptions.exceptions import InvalidQuestionId


@pytest.mark.django_db
def test_validate_question_id_with_valid_question_id(
        create_user,
        create_two_form_titles,
        create_questions):
    # arrnage
    question_id = 1
    questions_storage = QuestionStorageImplementation()
    is_valid_question_id = True

    # Act
    return_value = questions_storage.validate_question_id(
        question_id=question_id
    )

    # Assert
    assert is_valid_question_id == return_value


@pytest.mark.django_db
def test_validate_question_id_with_invalid_question_id(
        create_user,
        create_two_form_titles,
        create_questions):
    # arrnage
    invalid_question_id = 0
    questions_storage = QuestionStorageImplementation()
    is_valid_question_id = False

    # Act
    with pytest.raises(InvalidQuestionId):
        questions_storage.validate_question_id(
            question_id=invalid_question_id
        )
