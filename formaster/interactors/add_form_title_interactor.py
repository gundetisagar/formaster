from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.user_storage_interface import \
    UserStorageInterface
from django_swagger_utils.drf_server.exceptions import Forbidden


class AddFormTitleInteractor:
    def __init__(self, form_storage: FormStorageInterface,
                 user_storage: UserStorageInterface,
                 presenter: PresenterInterface):
        self.form_storage = form_storage
        self.user_storage = user_storage
        self.presenter = presenter

    def add_form_title(self, user_id: int, form_title: str):

        try:
            print(user_id)
            print(form_title)
            self.user_storage.validate_is_admin(user_id=user_id)

        except Forbidden:
            self.presenter.raise_exception_for_is_not_admin()
            return

        form_title_with_id_dto = self.form_storage.add_form_title(
            user_id=user_id,
            form_title=form_title
        )

        form_title_with_id_dict = self.presenter.add_form_title_response(
            form_title_with_id_dto
        )
        return form_title_with_id_dict
