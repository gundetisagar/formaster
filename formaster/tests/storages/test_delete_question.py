import pytest
from formaster.storages.question_storage_implementation import \
    QuestionStorageImplementation
from formaster.models import Question


@pytest.mark.django_db
def test_delete_question(create_user,
                         create_two_form_titles,
                         create_questions):
    # Arrange
    question_id = 1
    questions_storage = QuestionStorageImplementation()

    # Act
    questions_storage.delete_question(question_id=question_id)

    # Assert
    with pytest.raises(Question.DoesNotExist):
            Question.objects.get(id=question_id)
