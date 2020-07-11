from formaster_auth.interactors.storages.user_storage_interface import \
	UserStorageInterface
# from formaster_auth.interactors.presenters.presenter_interface import \
# 	PresenterInterface


class ValidateIsAdminInteractor:
	def __init__(self, user_storage: UserStorageInterface):
		self.user_storage = user_storage

	def validate_is_admin(self, user_id: int):
		is_user_admin = self.user_storage.validate_is_admin(user_id)
		return is_user_admin
