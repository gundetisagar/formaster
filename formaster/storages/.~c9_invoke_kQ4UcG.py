from formaster.constants.enums import QuestionTypes
from formaster.interactors.storages.question_storage_interface import \
    QuestionStorageInterface
from formaster.models.question import Question
from formaster.models.choices import Choices
from formaster.dtos.dtos import (
    FormWithQuestionsDto,
    QuestionResponseDto,
    QuestionDto
)
from formaster.exceptions.exceptions import InvalidQuestionId


class QuestionStorageImplementation(QuestionStorageInterface):

    def create_text_question(self,
                             question_type: QuestionTypes,
                             question_text: str,
                             required: bool,
                             description: str,
                             form_id: int):
        question = Question.objects.create(
            question_type=question_type,
            question_text=question_text,
            required=required,
            description=description,
            form_id=form_id
        )
        question_id = question.id
        return question_id

    def create_mcq_choices(self,
                           question_id: int,
                           choices_list: list):
        Choices.objects.bulk_create(
            Choices(question_id=question_id, choice_text=choice)
            for choice in choices_list
        )

    def validate_question_id(self, question_id: int) -> bool:
        try:
            Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise InvalidQuestionId
        return True

    def get_form_with_questions(self, form_id: int) -> FormWithQuestionsDto:
        question_query_set = Question.objects.filter(form_id=form_id)\
                                             .prefetch_related("choices_set")

        form_with_list_of_questions_dto = self._convert_question_query_set_to_dto(
            question_query_set
        )
        return form_with_list_of_questions_dto

    @staticmethod
    def _convert_choice_obj_to_dto(choice):
        from formaster.dtos.dtos import ChoiceDto
        choice_dto = ChoiceDto(
                choice_id=choice.id,
                choice_text=choice.choice_text
        )
        return choice_dto

    def _convert_question_query_set_to_dto(self, question_query_set):
        list_of_questions_dto = []
        if question_query_set:
            for question in question_query_set:
    
                choices_list = question.choices_set.all()
    
                list_of_choises_dto = []
    
                for choice in choices_list:
                    choice_dto = self._convert_choice_obj_to_dto(choice)
                    list_of_choises_dto.append(choice_dto)
    
                question_dto = self._convert_questions_obj_to_dto(
                    question,
                    list_of_choises_dto
                )
                list_of_questions_dto.append(question_dto)
            return list_of_questions_dto
        else:
            list_of_questions_dto

    @staticmethod
    def _convert_questions_obj_to_dto(question, list_of_choises_dto):
        from formaster.dtos.dtos import FormWithQuestionsDto
        form_with_questions_dto = FormWithQuestionsDto(
            form_id=question.form_id,
            form_title=question.form.form_title,
            question_id=question.id,
            question_type=question.question_type,
            question_text=question.question_text,
            required=question.required,
            description=question.description,
            choices=list_of_choises_dto
        )
        return form_with_questions_dto


    @staticmethod
    def _convert_choice_obj_to_dto(choice):
        from formaster.dtos.dtos import ChoiceDto
        choice_dto = ChoiceDto(
                choice_id=choice.id,
                choice_text=choice.choice_text
        )
        return choice_dto


    def get_form_view(self, form_id: int):
        questions_and_response_objs = \
            Question.objects.filter(form_id=form_id).prefetch_related("choices_set", 'response_set')
        list_of_view_from_response_dto = \
            self._convert_question_and_response_objs_to_dto(
                questions_and_response_objs
            )
        print("\n\n\n")
        print(list_of_view_from_response_dto)
        print("\n\n\n")
        return list_of_view_from_response_dto


    def _convert_question_and_response_objs_to_dto(
        self, questions_and_response_objs):
        list_of_question_and_answer_dto = []

        for question_obj in questions_and_response_objs:

            if question_obj.question_type in ['WELCOME_SCREEN', 'THANK_YOU_SCREEN']:
                question_dto = self._convert_question_mcq_obj_to_dto(question_obj)
                list_of_question_and_answer_dto.append(question_dto)


            if question_obj.question_type in ['MCQ', 'SMALL_TEXT', 'LARGE_TEXT']:
                choices_list = question_obj.choices_set.all()

                list_of_choises_dto = []

                for choice in choices_list:
                    choice_dto = self._convert_choice_obj_to_dto(choice)
                    list_of_choises_dto.append(choice_dto)
                    
                response = question_obj.response_set.all()
                response_obj = response[0]
                question_response_dto = self._convert_question_response_to_dto(
                    list_of_choises_dto, response_obj, question_obj
                )
                list_of_question_and_answer_dto.append(question_response_dto)
        return list_of_question_and_answer_dto



    @staticmethod
    def _convert_question_mcq_obj_to_dto(question_obj):
        question_dto = QuestionResponseDto(
            form_id=question_obj.form_id,
            form_title=question_obj.form.form_title,
            question_id=question_obj.id,
            question_type=question_obj.question_type,
            question_text=question_obj.question_text,
            required=question_obj.required,
            description=question_obj.description,
            choices=None,
            response_id=None,
            response_text=None,
            response_choice_id=None
        )
        return question_dto


    @staticmethod
    def _convert_question_response_to_dto(list_of_choises_dto,
                                          response_obj,
                                          question_obj):
        
        question_with_answer_dto = QuestionResponseDto(
            form_id=question_obj.form_id,
            form_title=question_obj.form.form_title,
            question_id=question_obj.id,
            question_type=question_obj.question_type,
            question_text=question_obj.question_text,
            required=question_obj.required,
            description=question_obj.description,
            choices=list_of_choises_dto,
            response_id=response_obj.id,
            response_text=response_obj.response_text,
            response_choice_id=response_obj.choice_id
        )
        return question_with_answer_dto


    #             choices_list = question.choices_set.all()
    
    #             list_of_choises_dto = []
    
    #             for choice in choices_list:
    #                 choice_dto = self._convert_choice_obj_to_dto(choice)
    #                 list_of_choises_dto.append(choice_dto)

    #         question_with_answer_dto = \
    #             self._convert_questions_obj_to_question_with_answer_dto(
    #                 question,
    #                 list_of_choises_dto
    #             )
    #         list_of_question_and_answer_dto.append(question_with_answer_dto)
    #     return list_of_question_and_answer_dto

    # @staticmethod
    # def _convert_questions_obj_to_question_with_answer_dto(
    #     question,
    #     list_of_choises_dto):
    #     response = question.response_set.all()
        
    #     # if response:
    #     response_obj = response[0]
    #     from formaster.dtos.dtos import ViewFormResponseDto
    #     question_with_answer_dto = ViewFormResponseDto(
    #         form_id=question.form_id,
    #         form_title=question.form.form_title,
    #         question_id=question.id,
    #         question_type=question.question_type,
    #         question_text=question.question_text,
    #         required=question.required,
    #         description=question.description,
    #         choices=list_of_choises_dto,
    #         response_id=response_obj.id,
    #         response_text=response_obj.response_text,
    #         response_choice_id=response_obj.choice_id
    #     )
    #     return question_with_answer_dto

    # def delete_question(self, question_id: int):
    #     question_obj = Question.objects.get(id=question_id)
    #     question_obj.delete()
