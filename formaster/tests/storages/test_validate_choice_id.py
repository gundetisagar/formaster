import pytest
from formaster.storages.choice_storage_implementation import \
    ChoiceStorageImplementation
from formaster.exceptions.exceptions import InvalidChoiceId


@pytest.mark.django_db
def test_validate_choice_id_with_valid_choice_id(
        create_user,
        create_two_form_titles,
        create_questions,
        create_choices):
    # arrnage
    choice_id = 1
    choice_storage = ChoiceStorageImplementation()
    is_valid_choice_id = True

    # Act
    return_value = choice_storage.validate_choice_id(
        choice_id=choice_id
    )

    # Assert
    assert is_valid_choice_id == return_value


@pytest.mark.django_db
def test_validate_choice_id_with_invalid_choice_id(
        create_user,
        create_two_form_titles,
        create_questions):
    # arrnage
    invalid_choice_id = 0
    choice_storage = ChoiceStorageImplementation()
    is_invalid_choice_id = False

    # Act
    with pytest.raises(InvalidChoiceId):
        choice_storage.validate_choice_id(
            choice_id=invalid_choice_id
        )
