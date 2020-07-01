import pytest
from formaster.dtos.dtos import (
    UserAuthTokensDto,
    FormTitleWithIdDto,
    UserDetailsDto,
    FormWithQuestionsDto,
    ChoiceDto,
    FormDetailsDto
    #ViewFormResponseDto
)
from formaster.constants.enums import QuestionTypes



@pytest.fixture()
def user_auth_token_dto():
    userauthdto = UserAuthTokensDto(
        user_id=1,
        access_token="12345",
        refresh_token="54321",
        expires_in=121313
    )
    return userauthdto


@pytest.fixture()
def user_profile_dtos():
    user_details_dto = UserDetailsDto(
        user_id=1,
        username="user",
        is_admin=True
    )
    return user_details_dto

@pytest.fixture()
def form_details_dto():
    form_details = FormDetailsDto(
        form_title="Sanck Form",
        form_id=1
    )
    return form_details


@pytest.fixture()
def form_title_with_id_dto():
    form_title_with_id = FormTitleWithIdDto(
        form_title="Sanck Form",
        form_id=1
    )
    return form_title_with_id


@pytest.fixture()
def form_title_with_id_two_dtos():
    list_of_dtos = []
    form_title_with_id_1 = FormTitleWithIdDto(
        form_title="Snacks Form",
        form_id=1
    )
    form_title_with_id_2 = FormTitleWithIdDto(
        form_title="Food Form",
        form_id=2
    )
    list_of_dtos.append(form_title_with_id_1)
    list_of_dtos.append(form_title_with_id_2)
    return list_of_dtos


#@pytest.fixture()
def list_of_choices_dtos():
    list_of_choice_1 = ChoiceDto(
        choice_id=1,
        choice_text="option A"
    )
    list_of_choice_2 = ChoiceDto(
        choice_id=2,
        choice_text="option B"
    )
    return [list_of_choice_1,list_of_choice_2]


@pytest.fixture()
def list_of_questions_dtos():
    list_of_questions_dto = FormWithQuestionsDto(
        form_id=1,
        form_title="Food form",
        question_id=1,
        question_type=QuestionTypes.LARGE_TEXT.value,
        question_text="what is your name?",
        required=True,
        description="About question",
        choices=list_of_choices_dtos()
    )
    return [list_of_questions_dto]


@pytest.fixture()
def list_of_questions_dict():
    choice_1 = {
        "choice_id": 1,
        "choice_text": "option A"
    }
    choice_2 = {
        "choice_id": 2,
        "choice_text": "option B"
    }
    choices_list = [choice_1, choice_2]
    list_of_questions = {
        "form_id": 1,
        "form_title": "Food form",
        "question_id": 1,
        "question_type": QuestionTypes.LARGE_TEXT.value,
        "question_text": "what is your name?",
        "required": True,
        "description": "About question",
        "choices": choices_list
    }
    return list_of_questions


# @pytest.fixture()
# def view_form_response_dto():
#     list_of_view_form_response_dto = [ViewFormResponseDto(
#         form_id=1,
#         form_title="food form",
#         question_id=1,
#         question_type=QuestionTypes.LARGE_TEXT.value,
#         question_text="what is your name?",
#         required=True,
#         description="About question",
#         choices=list_of_choices_dtos(),
#         response_id=1,
#         response_text="dummy name",
#         response_choice_id=1
#     )]
#     return list_of_view_form_response_dto

@pytest.fixture()
def view_from_response_dict():
    choice_1 = {
        "choice_id": 1,
        "choice_text": "option A"
    }
    choice_2 = {
        "choice_id": 2,
        "choice_text": "option B"
    }
    choices_list = [choice_1, choice_2]
    response_dict = {
        "form_id": 1,
        "form_title": "Food form",
        "question_and_response_list":[{
            "question_id": 1,
        "question_type": QuestionTypes.LARGE_TEXT.value,
        "question_text": "what is your name?",
        "required": True,
        "description": "About question",
        "choices": choices_list,
        "response_id": 1,
        "response_text": "dummy name",
        "response_choice_id": 1
        }]
    }
    return response_dict