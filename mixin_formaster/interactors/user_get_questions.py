
from mixin_formaster.interactors.storages.storage_interface import \
    StorageInterface
from mixin_formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from mixin_formaster.interactors.form_questions_interactor import \
    GetFormQuestionsInteractor
from mixin_formaster.interactors.mixins.form_validation import \
    FormValidationMixin
from mixin_formaster.dtos.dtos import ResponseDetailsDTO, \
    FormQuestionsAndResponseDetailsDTO


from mixin_formaster.exceptions.exceptions import FormDoesNotExist, \
    InvalidAccess


class UserGetQuestionsInteractor(FormValidationMixin):

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def user_get_questions_wrapper(self, user_id: int, form_id: int,
                                   presenter: PresenterInterface):
        try:
            return self._user_get_questions(user_id, form_id, presenter)
        except FormDoesNotExist:
            presenter.raise_form_does_not_exist_exception()
        except InvalidAccess:
            presenter.raise_user_can_not_access_to_form()


    def _user_get_questions(self,user_id: int, form_id: int,
                            presenter: PresenterInterface):
        form_questions_and_response_details = self.user_get_questions(
            user_id, form_id
        )
        response = presenter.user_get_questions_response(
            form_questions_and_response_details
        )
        return response

    def user_get_questions(self, user_id: int, form_id: int):

        self.is_valid_form_id(form_id)

        self.storage.is_user_access_to_form(user_id, form_id)

        from mixin_formaster.interactors.form_questions_interactor import \
            GetFormQuestionsInteractor

        form_questions_interactor = GetFormQuestionsInteractor(
            self.storage, form_id
        )

        form_questions_details_dto = form_questions_interactor.get_form_questions(form_id)

        list_of_questions_details = form_questions_details_dto.questions_details

        question_ids = [
            question.question_id
            for question in list_of_questions_details
        ]

        response_details_dto = self.storage.get_response_details(question_ids)

        form_questions_and_response_details = FormQuestionsAndResponseDetailsDTO(
            form_questions_details=form_questions_details_dto,
            response_details=response_details_dto
        )

        return form_questions_and_response_details
