from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.constants.exception_messages import (
    INVALID_USERNAME,
    INVALID_PASSWORD,
    INVALID_QUESTION_TYPE,
    INVALID_QUESTION_ID,
    INVALID_CHOICE_ID,
    INVALID_FORM_ID,
    INVALID_ACCESS,
    USER_IS_NOT_ADMIN,
    USER_IS_NOT_CREATER_OF_FORM,
    INVALID_RESPONSE_FORM
)
from formaster.exceptions.exceptions import (
    InvalidUsername,
    InvalidPassword,
    InvalidQuestionType,
    InvalidQuestionId,
    InvalidChoiceId,
    InvalidFormId,
    UserCannotDeleteFormException,
    UserCannotUpdateFormException,
    UserIsNotAdmin,
    UserIsNotCreaterOfForm,
    InvalidResponseForm
)
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    Unauthorized,
    Forbidden
)


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_username(self):
        raise NotFound(*INVALID_USERNAME)

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
