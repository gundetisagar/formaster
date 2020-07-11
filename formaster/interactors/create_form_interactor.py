from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import Forbidden

from formaster.adapters.service_adapter import service_adapter
from formaster_auth.exceptions.exceptions import UserIsNotAdmin, \
        UserDoesNotExist


class CreateFormInteractor:
    def __init__(self, form_storage: FormStorageInterface,
                 presenter: PresenterInterface):
        self.form_storage = form_storage
        self.presenter = presenter

    def create_form_wrapper(self, user_id: int, form_title: str,
                            presenter: PresenterInterface):
        try:
            return self._create_form_response(
                user_id=user_id,
                form_title=form_title,
                presenter=presenter
            )
        except UserDoesNotExist:
            self.presenter.raise_exception_for_invalid_user_id()
        except UserIsNotAdmin:
            self.presenter.raise_exception_for_user_is_not_admin()

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