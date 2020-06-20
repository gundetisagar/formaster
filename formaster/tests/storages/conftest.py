import pytest
#from datetime import datetime
#from freezegun import freeze_time
from formaster.models.user import User
from formaster.models.form import Form
from formaster.models.question import Question
from formaster.models.choices import Choices
from formaster.models.response import Response
from formaster.dtos.dtos import (
    FormTitleWithIdDto,
    FormWithQuestionsDto,
    ChoiceDto,
    #ViewFormResponseDto
)

from formaster.constants.enums import QuestionTypes


@pytest.fixture()
def create_user():
    user = User.objects.create(
        username="username",
        password="password",
        is_admin=True
    )
    user.set_password(user.password)
    user.save()

@pytest.fixture()
def create_second_user():
    user = User.objects.create(
        username="username_2",
        password="password_2",
        is_admin=False
    )
    user.set_password(user.password)
    user.save()

@pytest.fixture()
def create_two_form_titles():
    Form.objects.create(
        created_by_id=1,
        form_title="Snacks Form"
    )
    Form.objects.create(
        created_by_id=1,
        form_title="Food Form"
    )


@ pytest.fixture()
def create_questions():
    Question.objects.create(
        question_type=QuestionTypes.LARGE_TEXT.value,
        question_text="create question",
        required=True,
        description="about create question",
        form_id=1
    )

@pytest.fixture()
def create_mcq_question():
    Question.objects.create(
        question_type=QuestionTypes.MCQ.value,
        question_text="create question",
        required=True,
        description="about create question",
        form_id=1
    )


@pytest.fixture()
def create_choices():
    Choices.objects.create(
        question_id=1,
        choice_text="option A"
    )
    Choices.objects.create(
        question_id=1,
        choice_text="option B"
    )

@pytest.fixture()
def create_responses():
    Response.objects.create(
        response_by_id=2,
        question_id=1,
        response_text="my answer",
        choice_id=None
    )

@pytest.fixture()
def form_title_with_id_dto():
    form_title_with_id = FormTitleWithIdDto(
        form_title="Snacks Form",
        form_id=1
    )
    return form_title_with_id

@pytest.fixture()
def form_with_questions_dto():
    form_with_questions = [FormWithQuestionsDto(
        form_id=1,
        form_title='Snacks Form',
        question_id=1,
        question_type=QuestionTypes.LARGE_TEXT.value,
        question_text='create question',
        required=True,
        description='about create question',
        choices=[
            ChoiceDto(
                choice_id=1,
                choice_text='option A'),
            ChoiceDto(
                choice_id=2,
                choice_text='option B'
            )
        ]
    )]
    return form_with_questions


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



# @pytest.fixture()
# def view_form_response_dto():
#     list_of_view_form_response_dto = [ViewFormResponseDto(
#         form_id=1,
#         form_title="Snacks Form",
#         question_id=1,
#         question_type=QuestionTypes.LARGE_TEXT.value,
#         question_text="create question",
#         required=True,
#         description="about create question",
#         choices=[],
#         response_id=1,
#         response_text="my answer",
#         response_choice_id=None
#     )]
#     return list_of_view_form_response_dto