
from abc import ABC, abstractmethod
from mixin_formaster.dtos.dtos import FormDetailsDTO, QuestionDetailsDTO, \
    ChoiceDetailsDTO, FormQuestionsDetailsDTO, ResponseDetailsDTO
from typing import List


class StorageInterface(ABC):

    @abstractmethod
    def validate_question_id_with_form(self, question_id: int, form_id: int):
        pass

    @abstractmethod
    def is_valid_form_id(self, form_id: int):
        pass

    @abstractmethod
    def get_form(self, form_id: int):
        pass

    @abstractmethod
    def get_option_ids_for_question(self, question_id:int):
        pass

    @abstractmethod
    def create_user_mcq_response(self, user_id: int, question_id: int,
                                 user_submitted_option_id: int):
        pass

    @abstractmethod
    def validate_question_id(self, question_id: int) -> bool:
        pass

    @abstractmethod
    def get_form_details(self, form_id: int) -> FormDetailsDTO:
        pass

    @abstractmethod
    def get_question_ids(self, form_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_mcq_question_ids(self, question_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_choice_details(self, mcq_question_ids: List[int]) -> ChoiceDetailsDTO:
        pass

    @abstractmethod
    def get_questions_details(self, question_ids: List[int]) -> QuestionDetailsDTO:
        pass

    @abstractmethod
    def is_user_access_to_form(self, user_id: int, form_id: int):
        pass

    @abstractmethod
    def get_response_details(self, question_ids: List[int]) \
            -> List[ResponseDetailsDTO]:
        pass
