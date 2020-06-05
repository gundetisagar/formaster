from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster.storages.question_storage_implementation import \
    QuestionStorageImplementation
from formaster.storages.user_storage_implementation import \
    UserStorageImplementation
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation
from formaster.presenters.presenter_implementation import \
    PresenterImplementation
from formaster.interactors.delete_question_interactor import \
    DeleteQuestionInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user = kwargs['user']
    form_id = kwargs['form_id']
    question_id = kwargs['question_id']
    user_id = user.id

    form_storage = FormStorageImplimentation()
    questions_storage = QuestionStorageImplementation()
    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = DeleteQuestionInteractor(
        form_storage=form_storage,
        questions_storage=questions_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    interactor.delete_question(
        user_id=user_id,
        form_id=form_id,
        question_id=question_id
    )

    return HttpResponse(status=200)
