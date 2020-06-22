from mixin_formaster.interactors.storages.storage_interface import \
    StorageInterface
from mixin_formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from mixin_formaster.exceptions.exceptions import FormDoesNotExist
from mixin_formaster.interactors.mixins.form_validation import \
    FormValidationMixin
from mixin_formaster.dtos.dtos import FormQuestionsDetailsDTO


class GetFormQuestionsInteractor(FormValidationMixin):
    def __init__(self, form_id: int, storage: StorageInterface):
        self.storage = storage
        self.form_id = form_id

    def get_form_questions_wrapper(self,
                                   presenter: PresenterInterface):
        try:
            return self.get_form_questions(self.form_id)
        except FormDoesNotExist:
            presenter.raise_form_does_not_exist_exception()

    def get_form_questions(self, form_id: int):
        self.is_valid_form_id(self.form_id)

        form_details_dto = self.storage.get_form_details(self.form_id)

        question_ids = self.storage.get_question_ids(self.form_id)

        mcq_question_ids = self.storage.get_mcq_question_ids(question_ids)

        choice_details_dto = self.storage.get_choice_details(mcq_question_ids)

        questions_details_dto = self.storage.get_questions_details(question_ids)

        return FormQuestionsDetailsDTO(
            form_details=form_details_dto,
            questions_details=questions_details_dto,
            choice_details=choice_details_dto
        )
