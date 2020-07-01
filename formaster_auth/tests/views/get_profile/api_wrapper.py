import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from formaster_auth.storages.user_storage_implementation import \
    UserStorageImplementation
from formaster_auth.presenters.presenter_implementation import \
    PresenterImplementation
from formaster_auth.interactors.get_user_profile_interactor import \
    GetUserProfileInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

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
