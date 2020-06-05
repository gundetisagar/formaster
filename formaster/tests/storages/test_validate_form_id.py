import pytest
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation
from formaster.exceptions.exceptions import InvalidFormId


@pytest.mark.django_db
def test_validate_form_id_with_valid_form_id(
        create_user,
        create_two_form_titles):
    # arrnage
    form_id = 1
    form_storage = FormStorageImplimentation()
    is_valid_form_id = True

    # Act
    return_value = form_storage.validate_form_id(
        form_id=form_id
    )

    # Assert
    assert is_valid_form_id == return_value


@pytest.mark.django_db
def test_validate_form_id_with_invalid_form_id(
        create_user,
        create_two_form_titles):
    # arrnage
    invalid_form_id = 0
    form_storage = FormStorageImplimentation()

    # Act
    with pytest.raises(InvalidFormId):
        form_storage.validate_form_id(
            form_id=invalid_form_id
        )
