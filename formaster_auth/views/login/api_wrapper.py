from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster_auth.storages.user_storage_implementation import \
    UserStorageImplementation
from formaster_auth.presenters.presenter_implementation import \
    PresenterImplementation
from formaster_auth.interactors.login_interactor import \
    UserLoginInteractor
from formaster_auth.common.oauth2_storage import OAuth2SQLStorage
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    print(kwargs)
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']
    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage = OAuth2SQLStorage()

    interactor = UserLoginInteractor(
        user_storage=user_storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )

    access_details = interactor.user_login(
        username, password
    )
    response = json.dumps(access_details)
    return HttpResponse(response, status=200)