from abc import ABC, abstractmethod
from mixin_formaster.dtos.dtos import FormQuestionsAndResponseDetailsDTO


class PresenterInterface(ABC):

    @abstractmethod
    def submit_form_response_return(self, user_response_id: int):
        pass

    @abstractmethod
    def raise_form_does_not_exist_exception(self):
        pass

    @abstractmethod
    def raise_form_closed_exception(self):
        pass

    @abstractmethod
    def raise_question_does_not_belong_to_form_exception(self):
        pass

    @abstractmethod
    def raise_invalid_user_response_submitted(self):
        pass

    @abstractmethod
    def raise_question_does_not_exist_exception(self):
        pass

    @abstractmethod
    def user_get_questions_response(self,
            form_questions_and_response_details: FormQuestionsAndResponseDetailsDTO):
        pass
