

from mixin_formaster.exceptions.exceptions import FormClosed

class FormValidationMixin:

    def validate_for_live_form(self, form_id: int):
        form_dto = self.storage.get_form(form_id)
        # if not form_dto.is_live:
        #     raise FormClosed()
        # else:
        #     return True