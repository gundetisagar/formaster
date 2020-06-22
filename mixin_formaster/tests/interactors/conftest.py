import pytest
from mixin_formaster.dtos.dtos import FormDetailsDTO, QuestionDetailsDTO, \
    ChoiceDetailsDTO, FormQuestionsDetailsDTO, ResponseDetailsDTO, \
    FormQuestionsAndResponseDetailsDTO

@pytest.fixture()
def form_details_dto():
    form_details = FormDetailsDTO(
        form_id=1,
        form_name="form_name"
    )
    return form_details


@pytest.fixture()
def questions_details_dto():
    questions_details = [
        QuestionDetailsDTO(
            question_id=1,
            question_type="MCQ",
            question_text="first_question"
        ),
        QuestionDetailsDTO(
            question_id=2,
            question_type="MCQ",
            question_text="second_question"
        )
    ]
    return questions_details

@pytest.fixture()
def choice_details_dto():
    choice_details = [
        ChoiceDetailsDTO(
            question_id=1,
            choice_id=1,
            choice_text="A"
        ),
        ChoiceDetailsDTO(
            question_id=1,
            choice_id=2,
            choice_text="B"
        ),
        ChoiceDetailsDTO(
            question_id=2,
            choice_id=3,
            choice_text="A"
        ),
        ChoiceDetailsDTO(
            question_id=2,
            choice_id=4,
            choice_text="B"
        )
    ]
    return choice_details


@pytest.fixture()
def form_questions_details_dto():
    form_questions_details = FormQuestionsDetailsDTO(
        form_details=form_details_dto,
        questions_details=questions_details_dto,
        choice_details=choice_details_dto
    )
    return form_questions_details

@pytest.fixture()
def response_details_dto():
    response_details = [
        ResponseDetailsDTO(
            question_id=1,
            response_id=1,
            response_text=None,
            choice_id=1
        ),
        ResponseDetailsDTO(
            question_id=2,
            response_id=2,
            response_text=None,
            choice_id=4
        )
    ]
    return response_details

@pytest.fixture()
def form_questions_and_response_details_dto():
    form_questions_and_response_details = FormQuestionsAndResponseDetailsDTO(
        form_questions_details=form_questions_details_dto,
        response_details=response_details_dto
    )
    return form_questions_and_response_details