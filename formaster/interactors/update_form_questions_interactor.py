from formaster.interactors.storages.question_storage_interface import \
    QuestionStorageInterface
from formaster.constants.enums import QuestionTypes



class UpdateFormQuestionsInteractor:
    def __init__(self, question_storage: QuestionStorageInterface):
        self.question_storage = question_storage


    def update_form_questions(self,
                              form_id: int,
                              questions_list: list):

        pass
        # for question in questions_list:
        #     question_type = question["question_type"]
        #     question_text = question["question_text"]
        #     required = question["required"]
        #     description = question["description"]
        #     choices_list = question["choices_list"]

        #     question_id = self.question_storage.create_text_question(
        #         question_type=question_type,
        #         question_text=question_text,
        #         required=required,
        #         description=description,
        #         form_id=form_id,
        #     )

        #     if question_type == QuestionTypes.MCQ.value:
        #         self.question_storage.create_mcq_choices(
        #             question_id=question_id,
        #             choices_list=choices_list
        #         )
