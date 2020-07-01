from formaster_auth.interactors.storages.user_storage_interface import \
	UserStorageInterface


class ValidateUserIdInteractor:
	def __init__(self, user_storage: UserStorageInterface):
		self.user_storage = user_storage

	def validate_user_id(self, user_id: int):
		is_valid_user = self.user_storage.validate_user_id(user_id)
		return is_valid_user
