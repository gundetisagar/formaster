import pytest
from formaster_auth.presenters.presenter_implementation import \
    PresenterImplementation
from formaster_auth.constants.exception_messages import INVALID_USERNAME
from formaster_auth.exceptions.exceptions import InvalidUsername
from django_swagger_utils.drf_server.exceptions import NotFound

def test_raise_exception_for_invalid_username():
    # Arrange
    json_presenter = PresenterImplementation()
    exception_message = INVALID_USERNAME[0]
    exception_res_status = INVALID_USERNAME[1]

    # Act
    with pytest.raises(NotFound) as exception:
        json_presenter.raise_exception_for_invalid_username()

    # Act
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
