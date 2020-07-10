from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster_auth.constants.exception_messages import (
    INVALID_USERNAME,
    INVALID_PASSWORD,
    INVALID_ACCESS,
    USER_IS_NOT_ADMIN
)
from formaster_auth.exceptions.exceptions import (
    InvalidUsername,
    InvalidPassword,
    UserIsNotAdmin
)
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    Unauthorized,
    Forbidden
)

from django.http import response


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_username(self) -> response.HttpResponse:
        import json
        data = json.dumps({
            "response": INVALID_USERNAME[0],
            "http_status_code": 404,
            "res_status": INVALID_USERNAME[1]
        })
        response_object = response.HttpResponse(data, 404)
        return response_object
        #raise NotFound(*INVALID_USERNAME)

    # def raise_exception_for_invalid_comment_id(self) -> response.HttpResponse:
    #     from fb_post_clean_arch_v2.constants.exception_messages import \
    #         INVALID_COMMENT_ID
    #     import json
    #     data = json.dumps({
    #             "response": INVALID_COMMENT_ID[0],
    #             "http_status_code": 400,
    #             "res_status": INVALID_COMMENT_ID[1]
    #         })

    #     response_object = response.HttpResponse(data, 400)
    #     return response_object

    def raise_exception_for_invalid_password(self):
        raise Forbidden(*INVALID_PASSWORD)

    def raise_exception_for_is_not_admin(self):
        raise UserIsNotAdmin(*USER_IS_NOT_ADMIN)

    def user_login_response(self, tokens_dto, is_admin):
        login_access_dict = {
            "user_id": tokens_dto.user_id,
            "access_token": tokens_dto.access_token,
            "refresh_token": tokens_dto.refresh_token,
            "is_admin": is_admin
        }
        return login_access_dict

    def get_user_profile_response(self, user_profile_dto):
        user_profile_dict = {
            "user_id": user_profile_dto.user_id,
            "username": user_profile_dto.username,
            "is_admin": user_profile_dto.is_admin
        }
        return user_profile_dict
