import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster.interactors.login_interactor import UserLoginInteractor
from formaster.storages.user_storage_implementation import \
    UserStorageImplementation
from formaster.presenters.presenter_implementation import \
    PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

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

    token_details = interactor.user_login(
        username=username,
        password=password
    )
    response_data = json.dumps(token_details)
    return HttpResponse(response_data, status=200)
