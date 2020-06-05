from formaster.interactors.storages.user_storage_interface import \
	UserStorageInterface
from formaster.interactors.presenters.presenter_interface import \
	PresenterInterface



class GetUserProfileInteractor:
    def __init__(self, user_storage: UserStorageInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.presenter = presenter

    def get_user_profile(self, user_id: int):
        user_profile_dto = self.user_storage.get_user_profile(
            user_id=user_id
        )
        user_profile_dict = self.presenter.get_user_profile_response(
            user_profile_dto=user_profile_dto
        )
        return user_profile_dict
