from formaster.interactors.storages.question_storage_interface import \
    QuestionStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.constants.enums import QuestionTypes, LIST_OF_QUESTION_TYPES
from typing import List
from formaster.exceptions.exceptions import FormDoesNotExist, \
    InvalidQuestionType
from formaster.adapters.service_adapter import service_adapter

class CreateQuestionInteractor:
    def __init__(self, question_storage: QuestionStorageInterface,
                 presenter: PresenterInterface):
        self.question_storage = question_storage
        self.presenter = presenter

    def create_question_wrapper(self,
                                form_id: int,
                                questions_list: list
                                ):

        for question in questions_list:
            question_type = question["question_type"]
            question_text = question["question_text"]
            required = question["required"]
            description = question["description"]
            choices_list = question["choices_list"]

            question_id = self.question_storage.create_text_question(
                question_type=question_type,
                question_text=question_text,
                required=required,
                description=description,
                form_id=form_id,
            )

            if question_type == QuestionTypes.MCQ.value:
                self.question_storage.create_mcq_choices(
                    question_id=question_id,
                    choices_list=choices_list
                )

    # def create_question_wrapper(self, form_id: int, question_type: str,
    #         question_text: str, required: bool, description: str,
    #         choices_list: List[int], question_position: int,
    #         presenter: PresenterInterface):
    #     try:
    #         self.create_question(form_id=form_id, question_type=question_type,
    #                              question_text=question_text,
    #                              required=required, description=description,
    #                              choices_list=choices_list,
    #                              question_position=question_position)
    #     except FormDoesNotExist:
    #         presenter.raise_exception_for_invalid_form_id()




    # def create_question(self, form_id: int, question_type: str,
    #                     question_text: str, required: bool, description: str,
    #                     choices_list: List[int], question_position: int):

    #     service_adapter().user_service.validate_form_id(form_id=form_id)

    #     if question_type not in LIST_OF_QUESTION_TYPES:
    #         raise InvalidQuestionType