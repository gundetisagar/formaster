class UserService:
	@property
	def interface(self):
		from formaster_auth.interfaces.user_interface import UserInterface
		return UserInterface()

	def validate_user_id(self, user_id: int):
		self.interface.validate_user_id(user_id)
		#return is_valid_user

	def validate_is_admin(self, user_id: int):
		self.interface.validate_is_admin(user_id)
		#return is_user_admin
