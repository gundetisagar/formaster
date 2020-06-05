from dataclasses import dataclass
from typing import List


@dataclass()
class UserAuthTokensDto:
    user_id: int
    access_token: str
    refresh_token: str
    expires_in: int


@dataclass()
class UserDetailsDto:
    user_id: int
    username: str
    is_admin: bool

@dataclass()
class FormTitleWithIdDto:
    form_title: str
    form_id: int


@dataclass()
class ChoiceDto:
    choice_id: int
    choice_text: str



@dataclass()
class FormWithQuestionsDto:
    form_id: int
    form_title: str
    question_id: int
    question_type: str
    question_text: str
    required: bool
    description: str
    choices: List[ChoiceDto]

@dataclass()
class SubmitResponseDto:
    Question_id: int
    Answer: str
    choice_id: int


@dataclass()
class ResponseDto:
    response_id: int
    response_text: str
    response_choice_id: int
    response_choice_text: str


@dataclass()
class ViewFormResponseDto:
    form_id: int
    form_title: str
    question_id: int
    question_type: str
    question_text: str
    required: bool
    description: str
    choices: List[ChoiceDto]
    response_id: int
    response_text: str
    response_choice_id: int

