from formaster.interactors.storages.question_storage_interface import \
    QuestionStorageInterface
from formaster.interactors.storages.response_storage_interface import \
    ResponseStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound
from formaster.exceptions.exceptions import InvalidResponseForm


class ViewFormResponseInteractor:
    def __init__(self, question_storage: QuestionStorageInterface,
                 form_storage: FormStorageInterface,
                 presenter: PresenterInterface):
        self.question_storage = question_storage
        self.form_storage = form_storage
        self.presenter = presenter

    def get_form_view(self, form_id: int):
        try:
            self.form_storage.validate_form_id(
                form_id=form_id
            )
        except NotFound:
            self.presenter.raise_exception_for_invalid_form_id()
            return


        list_of_view_form_response_dto = self.question_storage.get_form_view(
            form_id=form_id
        )
        # except InvalidResponseForm:
        #     self.presenter.raise_exception_for_invalid_response_form()
        #     return

        form_response_dict = self.presenter.get_form_view_response(
            list_of_view_form_response_dto=list_of_view_form_response_dto
        )
        return form_response_dict


