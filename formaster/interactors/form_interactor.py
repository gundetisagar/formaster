from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import Forbidden, NotFound
from formaster.adapters.service_adapter import service_adapter
from formaster_auth.exceptions.exceptions import UserIsNotAdmin, \
        UserDoesNotExist
from formaster.exceptions.exceptions import (
    UserIsNotCreaterOfForm,
    FormDoesNotExist
)



class FormInteractor:
    def __init__(self, form_storage: FormStorageInterface):
        self.form_storage = form_storage

    def create_form_wrapper(self, user_id: int, form_title: str,
                            presenter: PresenterInterface):
        try:
            return self._create_form_response(
                user_id=user_id,
                form_title=form_title,
                presenter=presenter
            )
        except UserDoesNotExist:
            presenter.raise_exception_for_invalid_user_id()
        except UserIsNotAdmin:
            presenter.raise_exception_for_user_is_not_admin()

    def _create_form_response(self, user_id: int, form_title: str,
                                 presenter: PresenterInterface):
        form_details_dto = self.create_form(user_id=user_id,
                                               form_title=form_title)
        form_details_dict = presenter.create_form_response(
            form_details_dto=form_details_dto
        )
        return form_details_dict


    def create_form(self, user_id: int, form_title: str):

        service_adapter().user_service.validate_user_id(user_id)

        service_adapter().user_service.validate_is_admin(user_id)

        form_details_dto = self.form_storage.create_form(
            user_id=user_id,
            form_title=form_title
        )

        return form_details_dto


    def delete_form_wrapper(self, user_id: int, form_id: int,
                            presenter=PresenterInterface):
        try:
            self.delete_form(user_id=user_id, form_id=form_id)

        except UserDoesNotExist:
            presenter.raise_exception_for_invalid_user_id()

        except UserIsNotAdmin:
            presenter.raise_exception_for_user_is_not_admin()

        except FormDoesNotExist:
            presenter.raise_exception_for_invalid_form_id()

        except UserIsNotCreaterOfForm:
            presenter.raise_exception_for_user_is_not_creater_of_form()


    def delete_form(self, user_id: int, form_id: int):

        service_adapter().user_service.validate_user_id(user_id)

        service_adapter().user_service.validate_is_admin(user_id)

        self.form_storage.validate_form_id(form_id)

        self.form_storage.validate_is_user_creater_of_form(
                user_id=user_id, form_id=form_id
        )

        self.form_storage.delete_form(form_id=form_id)


    def get_forms_wrapper(self, user_id: int):
        pass

        # list_of_form_titles_with_id_dto = self.form_storage.get_forms(
        #     user_id=user_id
        # )

        # list_of_forms_dict = self.presenter.get_forms_response(
        #     list_of_form_titles_with_id_dto
        # )
        # return list_of_forms_dict

    def update_form_title_wrapper(self, user_id: int, form_id: int,
                                  new_form_title: str):
        pass
