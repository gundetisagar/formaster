import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster.interactors.update_form_title_interactor import \
    UpdateFormTitleInteractor
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation
from formaster.storages.user_storage_implementation import \
    UserStorageImplementation
from formaster.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.id
    form_id = kwargs['form_id']
    request_data = kwargs['request_data']
    new_form_title = request_data['new_form_title']

    form_storage = FormStorageImplimentation()
    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = UpdateFormTitleInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    form_title_with_id_dict = interactor.update_form_title(
        user_id=user_id,
        form_id=form_id,
        new_form_title=new_form_title
    )

    response_data = json.dumps(form_title_with_id_dict)
    return HttpResponse(response_data, status=201)
