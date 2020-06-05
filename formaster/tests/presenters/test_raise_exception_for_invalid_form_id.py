import pytest
from formaster.presenters.presenter_implementation import \
    PresenterImplementation

from formaster.constants.exception_messages import INVALID_FORM_ID
from formaster.exceptions.exceptions import InvalidFormId
from django_swagger_utils.drf_server.exceptions import NotFound

def test_raise_exception_for_invalid_form_id():
    # Arrange
    json_presenter = PresenterImplementation()
    exception_message = INVALID_FORM_ID[0]
    exception_res_status = INVALID_FORM_ID[1]

    # Act
    with pytest.raises(InvalidFormId) as exception:
        json_presenter.raise_exception_for_invalid_form_id()
