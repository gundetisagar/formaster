import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster.interactors.add_form_title_interactor import \
    AddFormTitleInteractor
from formaster.presenters.presenter_implementation import \
    PresenterImplementation
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user = kwargs['user']
    request_data = kwargs['request_data']
    form_title = request_data['form_title']
    user_id = user.id

    form_storage = FormStorageImplimentation()
    presenter = PresenterImplementation()

    interactor = AddFormTitleInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    form_details = interactor.add_form_title(
        user_id=user_id,
        form_title=form_title
    )

    response_data = json.dumps(form_details)
    return HttpResponse(response_data, status=201)

"""
    try:
        from formaster.views.add_form_title.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from formaster.views.add_form_title.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from formaster.views.add_form_title.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="formaster", test_case=test_case,
        operation_name="add_form_title",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
"""
