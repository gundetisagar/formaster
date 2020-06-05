import pytest
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation
from formaster.tests.interactors.conftest import form_title_with_id_two_dtos



@pytest.mark.django_db
def test_get_forms(create_user, create_two_form_titles,
                   form_title_with_id_two_dtos):
    # Arrange
    user_id = 1
    form_storage = FormStorageImplimentation()
    expected_form_details = form_title_with_id_two_dtos

    # Act
    return_value = form_storage.get_forms(
        user_id=user_id
    )

    # Assert
    assert expected_form_details == return_value
