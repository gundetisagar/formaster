import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster.interactors.get_user_forms_interactor import \
    GetUserFormsInteractor
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation
from formaster.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user_obj = kwargs['user']
    user_id = user_obj.id

    form_storage = FormStorageImplimentation()
    presenter = PresenterImplementation()

    interactor = GetUserFormsInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    list_of_form_titles_with_id_dict = interactor.get_user_forms(
        user_id=user_id
    )

    response_data = json.dumps(list_of_form_titles_with_id_dict)
    return HttpResponse(response_data, status=200)
