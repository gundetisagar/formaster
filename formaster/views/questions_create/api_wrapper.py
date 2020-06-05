import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster.interactors.questions_create_interactor import \
    QuestionsCreateInteractor
from formaster.storages.question_storage_implementation import \
    QuestionStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    print(kwargs,'"\n\n\n\n\n')
    user = kwargs['user']
    user_id = user.id
    form_id = kwargs['form_id']
    request_data = kwargs['request_data']
    questions_list = request_data['questions_create_list']

    question_storage = QuestionStorageImplementation()
    interactor = QuestionsCreateInteractor(
        question_storage=question_storage
    )

    interactor.questions_create(
        form_id=form_id,
        questions_list=questions_list
    )

    return HttpResponse(status=201)

"""
    try:
        from formaster.views.questions_create.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from formaster.views.questions_create.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from formaster.views.questions_create.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="formaster", test_case=test_case,
        operation_name="questions_create",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
"""
