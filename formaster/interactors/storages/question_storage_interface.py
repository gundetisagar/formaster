from typing import List
from abc import abstractmethod

from formaster.constants.enums import QuestionTypes
from formaster.dtos.dtos import (
    FormWithQuestionsDto,
    QuestionResponseDto
)


class QuestionStorageInterface:
    @abstractmethod
    def validate_question_id(self, question_id: int):
        pass

    @abstractmethod
    def create_text_question(self,
                             question_type: QuestionTypes,
                             question_text: str,
                             required: bool,
                             description: str,
                             form_id: int) -> int:
        pass

    @abstractmethod
    def create_mcq_choices(self,
                           question_id: str,
                           choices_list: list):
        pass

    @abstractmethod
    def get_form_with_questions(self, form_id: int) -> FormWithQuestionsDto:
        pass

    @abstractmethod
    def get_form_view(self, form_id:int) -> List[QuestionResponseDto]:
        pass

    @abstractmethod
    def delete_question(self, question_id: int):
        pass
