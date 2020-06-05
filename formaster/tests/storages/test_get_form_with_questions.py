import pytest
from formaster.storages.question_storage_implementation import \
    QuestionStorageImplementation




@pytest.mark.django_db
def test_get_form_with_questions(create_user,
                                 create_two_form_titles,
                                 create_questions,
                                 create_choices,
                                 form_with_questions_dto):
    # Arrange
    form_id = 1
    question_storage = QuestionStorageImplementation()
    expected_form_with_questions_dto = form_with_questions_dto

    # Act
    returns_dto = question_storage.get_form_with_questions(form_id=form_id)


    # Assert
    assert expected_form_with_questions_dto == returns_dto
