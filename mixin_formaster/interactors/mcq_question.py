from mixin_formaster.interactors.storages.storage_interface import \
    StorageInterface
from mixin_formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from mixin_formaster.interactors.base import BaseSubmitFormResponseInteractor
from mixin_formaster.exceptions.exceptions import InvalidUserResponseSubmit

from dataclasses import dataclass

@dataclass
class UserResponseDTO:
    user_id: int
    question_id: int
    user_submitted_option_id: int


class MCQQuestionSubmitFormResponseInteractor(
        BaseSubmitFormResponseInteractor):

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int, user_submitted_option_id: int):
        super().__init__(storage, question_id, form_id, user_id)
        self.user_submitted_option_id = user_submitted_option_id

    def _validate_user_response(self):
        option_ids = self.storage.get_option_ids_for_question(self.question_id)
        if self.user_submitted_option_id not in option_ids:
            raise InvalidUserResponseSubmit()

    def _validate_question_id(self):
        self.storage.validate_question_id(self.question_id)

    def _create_user_response(self) -> int:
        # user_response_dto = UserResponseDTO(
        #     self.user_id, self.question_id, self.user_submitted_option_id
        # )
        response_id = self.storage.create_user_mcq_response(
            self.user_id, self.question_id, self.user_submitted_option_id
        )
        return response_id
