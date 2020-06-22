

from mixin_formaster.exceptions.exceptions import FormClosed

class FormValidationMixin:

    def validate_for_live_form(self, form_id: int):
        form_dto = self.storage.get_form(form_id)
        if not form_dto.is_live:
            raise FormClosed()


    def is_valid_form_id(self, form_id: int):
        self.storage.is_valid_form_id(form_id)

    # def validate_is_user_admin(self, user_id: int, form_id: int):
    #     self.storage.is_user_admin(user_id, form_id)