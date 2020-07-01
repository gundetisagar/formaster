
from formaster_auth.storages.user_storage_implementation import \
	UserStorageImplementation

class UserInterface:
	@staticmethod
	def validate_is_admin(user_id: int):
		user_storage = UserStorageImplementation()
		from formaster_auth.interactors.validate_is_admin import \
			ValidateIsAdminInteractor
		interactor = ValidateIsAdminInteractor(
			user_storage=user_storage
		)
		is_user_admin = interactor.validate_is_admin(user_id)
		return is_user_admin

	@staticmethod
	def validate_user_id(user_id: int):
		user_storage = UserStorageImplementation()
		from formaster_auth.interactors.validate_user_id import \
			ValidateUserIdInteractor
		interactor = ValidateUserIdInteractor(
			user_storage=user_storage
		)
		is_valid_user = interactor.validate_user_id(user_id)
		return is_valid_user
