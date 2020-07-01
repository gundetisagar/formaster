from formaster_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface
from formaster_auth.interactors.presenters.presenter_interface import \
    PresenterInterface
from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from formaster_auth.exceptions.exceptions import InvalidPassword, InvalidUsername



class UserLoginInteractor:
    def __init__(self, user_storage: UserStorageInterface,
                 presenter: PresenterInterface,
                 oauth_storage: OAuthUserAuthTokensService):
        self.user_storage = user_storage
        self.presenter = presenter
        self.oauth_storage = oauth_storage

    def user_login(self, username: str, password: str):

        try:
            self.user_storage.validate_username(
                username=username
            )
        except InvalidUsername:
            self.presenter.raise_exception_for_invalid_username()
            return

        try:
            user_obj = self.user_storage.validate_password(
                username=username,
                password=password
            )
        except InvalidPassword:
            self.presenter.raise_exception_for_invalid_password()
            return

        service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth_storage
        )

        user_id = user_obj.id
        is_admin = user_obj.is_admin

        tokens_dto = service.create_user_auth_tokens(
            user_id=user_id
        )

        return self.presenter.user_login_response(tokens_dto, is_admin)
