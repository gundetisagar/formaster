from typing import List
from dataclasses import dataclass

@dataclass()
class FormDetailsDTO:
    form_id: int
    form_name: str

@dataclass()
class QuestionDetailsDTO:
    question_id: int
    question_type: str
    question_text: str

@dataclass()
class ChoiceDetailsDTO:
    question_id: int
    choice_id: int
    choice_text: str


@dataclass()
class FormQuestionsDetailsDTO:
    form_details: FormDetailsDTO
    questions_details:List[QuestionDetailsDTO]
    choice_details: List[ChoiceDetailsDTO]


@dataclass
class ResponseDetailsDTO:
    question_id: int
    response_id: int
    response_text: str
    choice_id: int

@dataclass
class FormQuestionsAndResponseDetailsDTO:
    form_questions_details: FormQuestionsDetailsDTO
    response_details: List[ResponseDetailsDTO]
