from formaster.interactors.storages.question_storage_interface import \
	QuestionStorageInterface
from formaster.interactors.presenters.presenter_interface import \
	PresenterInterface



class GetFormWithQuestionsInteractor:
    def __init__(self, question_storage: QuestionStorageInterface,
                 presenter: PresenterInterface):
        self.question_storage = question_storage
        self.presenter = presenter

    def get_form_with_questions(self, form_id: int):
        form_with_list_of_questions_dto = \
            self.question_storage.get_form_with_questions(
                form_id=form_id
            )

        form_with_list_of_questions_dict = \
            self.presenter.get_form_with_questions_response(
                form_with_list_of_questions_dto=form_with_list_of_questions_dto
            )
        return form_with_list_of_questions_dict
