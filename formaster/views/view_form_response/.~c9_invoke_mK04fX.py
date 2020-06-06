import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster.interactors.view_form_response_interactor import \
    ViewFormResponseInteractor
from formaster.storages.question_storage_implementation import \
    QuestionStorageImplementation
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation
from formaster.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    form_id = kwargs['form_id']

    form_storage = FormStorageImplimentation()
    question_storage = QuestionStorageImplementation()
    presenter = PresenterImplementation()

    interactor = ViewFormResponseInteractor(
        question_storage=question_storage,
        form_storage=form_storage,
        presenter=presenter
    )

    view_response_dict  = interactor.get_form_view(form_id=form_id)

    response_data = json.dumps(view_response_dict)
    return HttpResponse(response_data, status=200)



"""
from formaster.interactors.view_form_response_interactor import \
    ViewFormResponseInteractor
from formaster.storages.question_storage_implementation import \
    QuestionStorageImplementation
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation
from formaster.presenters.presenter_implementation import \
    PresenterImplementation
form_storage = FormStorageImplimentation()
    question_storage = QuestionStorageImplementation()
    presenter = PresenterImplementation()

    interactor = ViewFormResponseInteractor(
        question_storage=question_storage,
        form_storage=form_storage,
        presenter=presenter
    )


"""
























































