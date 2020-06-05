from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.user_storage_interface import \
    UserStorageInterface
from formaster.interactors.storages.question_storage_interface import \
    QuestionStorageInterface
from formaster.exceptions.exceptions import (
    UserIsNotCreaterOfForm,
    UserIsNotAdmin,
    InvalidFormId,
    InvalidQuestionId
)


class DeleteQuestionInteractor:
    def __init__(self, form_storage: FormStorageInterface,
                 questions_storage: QuestionStorageInterface,
                 user_storage: UserStorageInterface,
                 presenter: PresenterInterface):
        self.form_storage = form_storage
        self.questions_storage = questions_storage
        self.user_storage = user_storage
        self.presenter = presenter

    def delete_question(self, user_id:int, form_id: int, question_id: int):
        try:
            self.questions_storage.validate_question_id(
                question_id=question_id
            )
        except InvalidQuestionId:
            self.presenter.raise_exception_for_invalid_question_id()
            return

        try:
            self.user_storage.validate_is_admin(user_id=user_id)
        except UserIsNotAdmin:
            self.presenter.raise_exception_for_is_not_admin()
            return

        try:
            self.form_storage.validate_form_id(form_id=form_id)
        except InvalidFormId:
            self.presenter.raise_exception_for_invalid_form_id()
            return

        try:
            self.form_storage.validate_is_user_creater_of_form(
                user_id=user_id, form_id=form_id
            )
        except UserIsNotCreaterOfForm:
            self.presenter.raise_exception_for_user_cannot_delete_form()
            return

        self.questions_storage.delete_question(question_id=question_id)
