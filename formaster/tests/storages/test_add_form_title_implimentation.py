import pytest
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation


@pytest.mark.django_db
def test_add_form_title_with_valid_details(create_user,
                                           form_title_with_id_dto):
    # Arrange
    user_id = 1
    form_title = "Snacks Form"
    form_storage = FormStorageImplimentation()
    expected_form_details = form_title_with_id_dto

    # Act
    return_value = form_storage.add_form_title(
        user_id=user_id,
        form_title=form_title
    )

    # Assert
    assert expected_form_details == return_value
