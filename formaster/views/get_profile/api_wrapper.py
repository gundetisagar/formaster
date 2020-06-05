import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster.storages.user_storage_implementation import \
    UserStorageImplementation
from formaster.presenters.presenter_implementation import \
    PresenterImplementation
from formaster.interactors.get_user_profile_interactor import \
    GetUserProfileInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user = kwargs['user']
    user_id = user.id

    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetUserProfileInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    user_profile_dict = interactor.get_user_profile(user_id=user_id)

    response_data = json.dumps(user_profile_dict)
    return HttpResponse(response_data, status=200)

"""
    try:
        from formaster.views.get_profile.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from formaster.views.get_profile.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from formaster.views.get_profile.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="formaster", test_case=test_case,
        operation_name="get_profile",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
"""
