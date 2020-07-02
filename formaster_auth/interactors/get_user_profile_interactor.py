from formaster_auth.interactors.storages.user_storage_interface import \
	UserStorageInterface
from formaster_auth.interactors.presenters.presenter_interface import \
	PresenterInterface
from formaster_auth.exceptions.exceptions import UserDoesNotExist


class GetUserProfileInteractor:
    def __init__(self, user_storage: UserStorageInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.presenter = presenter

    def get_user_profile_wrapper(self, user_id: int,
                                 presenter: PresenterInterface):
        try:
            return self._get_user_profile_response(
                user_id=user_id,
                presenter=presenter
            )
        except UserDoesNotExist:
            presenter.raise_exception_for_user_does_not_exist()

    def _get_user_profile_response(self, user_id: int,
                                   presenter: PresenterInterface):
        user_profile_dto = self.get_user_profile(user_id)
        user_profile_dict = presenter.get_user_profile_response(
            user_profile_dto
        )
        return user_profile_dict

    def get_user_profile(self, user_id: int):

        is_valid_user = self.user_storage.validate_user_id(user_id)
        is_invalid_user = not is_valid_user
        if is_invalid_user:
            raise UserDoesNotExist

        user_profile_dto = self.user_storage.get_user_profile(user_id)

        return user_profile_dto
