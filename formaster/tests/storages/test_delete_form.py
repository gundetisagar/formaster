import pytest
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation
from formaster.models.form import Form


@pytest.mark.django_db
def test_delete_form(create_two_form_titles):
    # Arrange
    form_id = 1
    form_storage = FormStorageImplimentation()

    # Act
    form_storage.delete_form(form_id=form_id)

    # Assert
    with pytest.raises(Form.DoesNotExist):
            Form.objects.get(id=form_id)
