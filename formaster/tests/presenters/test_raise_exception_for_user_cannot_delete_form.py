import pytest
from formaster.presenters.presenter_implementation import \
    PresenterImplementation

from formaster.exceptions.exceptions import UserIsNotCreaterOfForm


def test_raise_exception_for_user_cannot_delete_form():
    # Arrange
    json_presenter = PresenterImplementation()


    # Act
    with pytest.raises(UserIsNotCreaterOfForm):
        json_presenter.raise_exception_for_user_cannot_delete_form()
