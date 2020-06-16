import pytest
from formaster.dtos.dtos import (
    FormTitleWithIdDto,
    UserDetailsDto,
    FormWithQuestionsDto,
    ChoiceDto,
    #ViewFormResponseDto
)
from formaster.constants.enums import QuestionTypes



@pytest.fixture()
def user_profile_dto():
    user_details_dto = UserDetailsDto(
        user_id=1,
        username="user",
        is_admin=True
    )
    return user_details_dto

@pytest.fixture()
def form_title_with_id_dto():
    form_title_with_id = FormTitleWithIdDto(
        form_title="Snacks Form",
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


@pytest.fixture()
def expected_form_details():
    expected_form_details_dict = [
        {
            "form_title": "Snacks Form",
            "form_id": 1
        },
        {
            "form_title": "Food Form",
            "form_id": 2
        }
    ]
    forms_list_dict =  {
        "forms_list": expected_form_details_dict
    }
    return forms_list_dict


@pytest.fixture()
def form_with_questions_dto():
    form_with_questions = FormWithQuestionsDto(
        form_id=1,
        form_title='Snacks Form',
        question_id=1,
        question_type=QuestionTypes.LARGE_TEXT.value,
        question_text='what is your name?',
        required=True,
        description='About question',
        choices=[
            ChoiceDto(
                choice_id=1,
                choice_text='option A'),
            ChoiceDto(
                choice_id=2, 
                choice_text='option B'
            )
        ]
    )
    return [form_with_questions]

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
        "form_title": "Snacks Form",
        "question_and_response_list": [{
            "question_id": 1,
            "question_type": QuestionTypes.LARGE_TEXT.value,
            "question_text": "what is your name?",
            "required": True,
            "description": "About question",
            "choices": choices_list
        }]
    }
    return list_of_questions


@pytest.fixture()
def view_form_response_text_question_dto():
    list_of_view_form_response_dto = [ViewFormResponseDto(
        form_id=1,
        form_title="Snacks Form",
        question_id=1,
        question_type=QuestionTypes.LARGE_TEXT.value,
        question_text="create question",
        required=True,
        description="about create question",
        choices=[],
        response_id=1,
        response_text="my answer",
        response_choice_id=None
    )]
    return list_of_view_form_response_dto

# @pytest.fixture()
# def view_form_response_mcq_question_dto():
#     choice_1 = ChoiceDto(
#         choice_id=1,
#         choice_text="option A"
#     )
#     choice_2 = ChoiceDto(
#         choice_id=2,
#         choice_text="option B"
#     )
#     choices_list = [choice_1, choice_2]
#     list_of_view_form_response_dto = [ViewFormResponseDto(
#         form_id=1,
#         form_title="Snacks Form",
#         question_id=1,
#         question_type=QuestionTypes.MCQ.value,
#         question_text="quantity of packets",
#         required=True,
#         description=None,
#         choices=choices_list,
#         response_id=1,
#         response_text=None,
#         response_choice_id=1
#     )]
#     return list_of_view_form_response_dto

