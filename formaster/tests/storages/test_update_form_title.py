import pytest
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation
from formaster.models import Form


@pytest.mark.django_db
def test_update_form_title(create_user, create_two_form_titles):
    # Arrange
    form_id = 1
    new_form_title = "New Form Title"
    form_storage = FormStorageImplimentation()

    # Act
    form_storage.update_form_title(
        form_id=form_id,
        new_form_title=new_form_title
    )

    # Assert
    form_obj = Form.objects.get(id=form_id)
    assert new_form_title == form_obj.form_title
