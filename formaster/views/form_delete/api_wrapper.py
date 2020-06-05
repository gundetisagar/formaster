import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster.interactors.delete_form_interactor import \
    DeleteFormInteractor
from formaster.storages.user_storage_implementation import \
    UserStorageImplementation
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation
from formaster.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user = kwargs['user']
    user_id = user.id
    form_id = kwargs['form_id']

    user_storage = UserStorageImplementation()
    form_storage = FormStorageImplimentation()
    presenter = PresenterImplementation()

    interactor = DeleteFormInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    interactor.delete_form(user_id=user_id, form_id=form_id)

    return HttpResponse(status=200)
