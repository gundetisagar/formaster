from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.user_storage_interface import \
    UserStorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from formaster.exceptions.exceptions import (
    UserIsNotCreaterOfForm,
    UserIsNotAdmin,
    InvalidFormId
)


class DeleteFormInteractor:
    def __init__(self, form_storage: FormStorageInterface,
                 user_storage: UserStorageInterface,
                 presenter: PresenterInterface):
        self.form_storage = form_storage
        self.user_storage = user_storage
        self.presenter = presenter

    def delete_form(self, user_id:int, form_id: int):
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

        self.form_storage.delete_form(form_id=form_id)
