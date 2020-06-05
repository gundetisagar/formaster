import pytest
from formaster.storages.response_storage_implementation import \
    ResponseStorageImplementation
from formaster.models.response import Response



@pytest.mark.django_db
def test_submit_response_with_choice_none(
            create_user,
            create_two_form_titles,
            create_questions):
    # Arrange
    user_id = 1
    question_id = 1
    response_text = "Answer_1"
    choice_id = None
    response_id = 1
    response_storage = ResponseStorageImplementation()

    # Act
    response_storage.submit_response(
        user_id=user_id,
        question_id=question_id,
        response_text=response_text,
        choice_id=choice_id
    )

    # Assert
    response_obj = Response.objects.get(response_by_id=user_id, question_id=question_id)
    assert question_id == response_obj.question_id
    assert response_id == response_obj.id
    assert user_id == response_obj.response_by_id
    assert response_text == response_obj.response_text
    assert choice_id == response_obj.choice_id


@pytest.mark.django_db
def test_submit_response_with_response_text_none(
            create_user,
            create_two_form_titles,
            create_mcq_question,
            create_choices):
    # Arrange
    user_id = 1
    question_id = 1
    response_text = None
    choice_id = 1
    response_id = 1
    response_storage = ResponseStorageImplementation()

    # Act
    response_storage.submit_response(
        user_id=user_id,
        question_id=question_id,
        response_text=response_text,
        choice_id=choice_id
    )

    # Assert
    response_obj = Response.objects.get(response_by_id=user_id, question_id=question_id)
    assert question_id == response_obj.question_id
    assert response_id == response_obj.id
    assert user_id == response_obj.response_by_id
    assert response_text == response_obj.response_text
    assert choice_id == response_obj.choice_id
