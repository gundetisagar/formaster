import pytest
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation
from formaster.exceptions.exceptions import UserIsNotCreaterOfForm

@pytest.mark.django_db
def test_validate_is_user_creater_of_form_with_invalid_user_returns_false(
        create_user,
        create_two_form_titles):
    # arrnage
    invalid_user_id = 0
    form_id = 1
    form_storage = FormStorageImplimentation()
    is_user_not_create_of_form = False

    # Act
    with pytest.raises(UserIsNotCreaterOfForm):
        form_storage.validate_is_user_creater_of_form(
            user_id=invalid_user_id,
            form_id=form_id
        )

    # # Assert
    # assert is_user_not_create_of_form == return_value


@pytest.mark.django_db
def test_validate_is_user_creater_of_form_with_valid_user_returns_true(
        create_user,
        create_two_form_titles):
    # arrnage
    user_id = 1
    form_id = 1
    form_storage = FormStorageImplimentation()
    is_user_creater_of_form = True

    # Act
    
    return_value = form_storage.validate_is_user_creater_of_form(
        user_id=user_id,
        form_id=form_id
    )

    # Assert
    assert is_user_creater_of_form == return_value
