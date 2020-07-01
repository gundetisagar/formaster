
from unittest.mock import create_autospec, patch
import pytest
from formaster_auth.interactors.login_interactor import UserLoginInteractor
from formaster_auth.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface
from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from common.oauth2_storage import OAuth2SQLStorage
from formaster_auth.exceptions.exceptions import InvalidUsername, InvalidPassword




def test_user_login_with_invalid_username():
    # Arrange
    username = "sagar"
    password = "1234"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuthUserAuthTokensService)

    user_storage.validate_username.side_effect = InvalidUsername
    presenter.raise_exception_for_invalid_username.side_effect = \
        InvalidUsername
    interactor = UserLoginInteractor(
        user_storage=user_storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )

    # Act
    with pytest.raises(InvalidUsername):
        interactor.user_login(
            username=username,
            password=password
        )
    # Assert
    presenter.raise_exception_for_invalid_username.assert_called_once()
    user_storage.validate_username.assert_called_once_with(username=username)


def test_user_login_with_invalid_password():
    # Arrange
    username = "sagar"
    password = "1234"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuthUserAuthTokensService)

    user_storage.validate_password.side_effect = InvalidPassword
    presenter.raise_exception_for_invalid_password.side_effect = \
        InvalidPassword
    interactor = UserLoginInteractor(
        user_storage=user_storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )

    # Act
    with pytest.raises(InvalidPassword):
        interactor.user_login(
            username=username,
            password=password
        )
    # Assert
    presenter.raise_exception_for_invalid_password.assert_called_once()
    user_storage.validate_username.assert_called_once_with(username=username)
    user_storage.validate_password.assert_called_once_with(
        username=username,
        password=password
    )



@patch("common.oauth_user_auth_tokens_service.OAuthUserAuthTokensService.create_user_auth_tokens")
def test_user_login_interactor(userauthtokendto):
    # Arrange
    username = "sagar"
    password = "123"
    user_id = 1
    class UserObject:
        id = 1,
        is_admin = True
    user_obj = UserObject()

    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuthUserAuthTokensService)
    oauth2_storage = create_autospec(OAuth2SQLStorage)

    user_storage.validate_username.return_value = True
    user_storage.validate_password.return_value = user_obj
    presenter.user_login_response.return_value = userauthtokendto
    oauth_storage.create_user_auth_tokens.return_value = userauthtokendto

    interactor = UserLoginInteractor(
        user_storage=user_storage,
        presenter=presenter,
        oauth_storage=oauth2_storage
    )
    # Act
    servive = interactor.user_login(
        username=username,
        password=password
    )

    # Assert
    assert servive == userauthtokendto
    user_storage.validate_username.assert_called_once_with(username=username)
    user_storage.validate_password.assert_called_once_with(
        username=username,
        password=password
    )
    oauth_storage.create_user_auth_tokens.assert_called_once_with(
        user_id=user_id
    )
