from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster.interactors.submit_response_interactor import \
    SubmitResponseInteractor
from formaster.storages.response_storage_implementation import \
    ResponseStorageImplementation
from formaster.storages.question_storage_implementation import \
    QuestionStorageImplementation
from formaster.storages.choice_storage_implementation import \
    ChoiceStorageImplementation
from formaster.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user_obj = kwargs['user']
    user_id = user_obj.id
    request_data = kwargs['request_data']
    response_list = request_data['response_list']

    response_storage = ResponseStorageImplementation()
    questions_storage = QuestionStorageImplementation()
    choice_storage = ChoiceStorageImplementation()
    presenter = PresenterImplementation()

    interactor = SubmitResponseInteractor(
        response_storage=response_storage,
        questions_storage=questions_storage,
        choice_storage=choice_storage,
        presenter=presenter
    )

    interactor.submit_response(user_id=user_id, response_list=response_list)

    return HttpResponse(status=201)
