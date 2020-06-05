import pytest
from formaster.presenters.presenter_implementation import \
    PresenterImplementation

from formaster.constants.exception_messages import INVALID_ACCESS
from formaster.exceptions.exceptions import InvalidUserId, UserIsNotAdmin
from django_swagger_utils.drf_server.exceptions import Forbidden


def test_raise_exception_for_is_not_admin():
    # Arrange
    json_presenter = PresenterImplementation()
    exception_message = INVALID_ACCESS[0]
    exception_res_status = INVALID_ACCESS[1]

    # Act
    with pytest.raises(UserIsNotAdmin) as exception:
        json_presenter.raise_exception_for_is_not_admin()

    # # Act
    # assert exception.value.message == exception_message
    # assert exception.value.res_status == exception_res_status
