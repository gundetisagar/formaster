import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster.interactors.get_forms_interactor import \
    GetFormsInteractor
from formaster.presenters.presenter_implementation import \
    PresenterImplementation
from formaster.storages.form_storage_implementation import \
    FormStorageImplimentation



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user = kwargs['user']
    user_id = user.id
    form_storage = FormStorageImplimentation()
    presenter = PresenterImplementation()

    interactor = GetFormsInteractor(
        form_storage=form_storage,
        presenter=presenter
    )

    forms_list = interactor.get_forms(user_id=user_id)

    response_data = json.dumps(forms_list)
    return HttpResponse(response_data, status=200)


"""
    try:
        from formaster.views.get_form.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from formaster.views.get_form.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from formaster.views.get_form.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="formaster", test_case=test_case,
        operation_name="get_form",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
"""
