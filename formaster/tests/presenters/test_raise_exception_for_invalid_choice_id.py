import pytest
from formaster.presenters.presenter_implementation import \
    PresenterImplementation
from formaster.constants.exception_messages import INVALID_CHOICE_ID
from django_swagger_utils.drf_server.exceptions import NotFound


def test_raise_exception_for_invalid_choice_id():
    # Arrange
    json_presenter = PresenterImplementation()
    exception_message = INVALID_CHOICE_ID[0]
    exception_res_status = INVALID_CHOICE_ID[1]

    # Act
    with pytest.raises(NotFound) as exception:
        json_presenter.raise_exception_for_invalid_choice_id()

    # Act
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
