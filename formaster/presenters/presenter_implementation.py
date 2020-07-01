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

    def raise_exception_for_invalid_question_type(self):
        raise InvalidQuestionType(*INVALID_QUESTION_TYPE)

    def raise_exception_for_invalid_question_id(self):
        raise NotFound(*INVALID_QUESTION_ID)

    def raise_exception_for_invalid_choice_id(self):
        raise NotFound(*INVALID_CHOICE_ID)

    def raise_exception_for_invalid_form_id(self):
        raise InvalidFormId(*INVALID_FORM_ID)

    def raise_exception_for_user_cannot_delete_form(self):
        raise UserIsNotCreaterOfForm(*USER_IS_NOT_CREATER_OF_FORM)

    def raise_exception_for_user_cannot_update_form(self):
        raise UserIsNotCreaterOfForm(*USER_IS_NOT_CREATER_OF_FORM)

    def raise_exception_for_is_not_admin(self):
        raise UserIsNotAdmin(*USER_IS_NOT_ADMIN)

    def raise_exception_for_invalid_response_form(self):
        raise InvalidResponseForm(*INVALID_RESPONSE_FORM)



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

    def add_form_title_response(self, form_details_dto):
        form_details_dict = self._convert_form_details_dto_to_dict(
            form_details_dto)
        return form_details_dict


    def get_forms_response(self, list_of_form_titles_with_id_dto):
        list_of_form_details_dict = []
        for form_details_dto in list_of_form_titles_with_id_dto:
            form_details_dict = \
                        self._convert_form_details_dto_to_dict(
                            form_details_dto
                        )
            list_of_form_details_dict.append(form_details_dict)
        list_forms_dict = {
            "forms_list": list_of_form_details_dict
        }
        return list_forms_dict

    def get_user_forms_response(self, list_of_form_titles_with_id_dto):
        list_of_form_details_dict = []
        for form_details_dto in list_of_form_titles_with_id_dto:
            form_details_dict = \
                        self._convert_form_details_dto_to_dict(
                            form_details_dto
                        )
            list_of_form_details_dict.append(form_details_dict)
        list_forms_dict = {
            "forms_list": list_of_form_details_dict
        }
        return list_forms_dict


    def _convert_form_details_dto_to_dict(self, form_details_dto):
        form_details_dict = {
            "form_title": form_details_dto.form_title,
            "form_id": form_details_dto.form_id
        }
        return form_details_dict


    def get_form_with_questions_response(self,
                                         form_with_list_of_questions_dto):
        list_of_questions_dict = []
        if form_with_list_of_questions_dto:
            for question in form_with_list_of_questions_dto:

                choices = question.choices
                choices_list = []
                for choice in choices:
                    choice = {
                        "choice_id": choice.choice_id,
                        "choice_text": choice.choice_text
                    }
                    choices_list.append(choice)

                question_dict = {
                    "question_id": question.question_id,
                    "question_type": question.question_type,
                    "question_text": question.question_text,
                    "required": question.required,
                    "description": question.description,
                    "choices": choices_list
                }
                list_of_questions_dict.append(question_dict)
            form_id = form_with_list_of_questions_dto[0].form_id
            form_title = form_with_list_of_questions_dto[0].form_title
            list_of_form_question_dict = {
                "form_id": form_id,
                "form_title": form_title,
                "question_and_response_list": list_of_questions_dict
            }
            return list_of_form_question_dict
        else:
            return {}

    def _convert_question_dto_to_dict(self):
        pass

    def get_form_view_response(self, list_of_view_form_response_dto):
        list_of_question_responses = []
        for response in list_of_view_form_response_dto:
            choices_list = []
            if response.choices:
                choices = response.choices
                for choice in choices:
                    choice = {
                        "choice_id": choice.choice_id,
                        "choice_text": choice.choice_text
                    }
                    choices_list.append(choice)
            view_response_dict = {
                "question_id": response.question_id,
                "question_type": response.question_type,
                "question_text": response.question_text,
                "required": response.required,
                "description": response.description,
                "choices": choices_list,
                "response_id": response.response_id,
                "response_text": response.response_text,
                "response_choice_id": response.response_choice_id
            }
            list_of_question_responses.append(view_response_dict)

        form_question_and_response_dict = {
            "form_id": list_of_view_form_response_dto[0].form_id,
            "form_title": list_of_view_form_response_dto[0].form_title,
            "question_and_response_list": list_of_question_responses
        }
        return form_question_and_response_dict


    def update_form_title_response(self, form_details_dto):
        form_details_dict = \
            self._convert_form_details_dto_to_dict(
                form_details_dto
            )
        return form_details_dict
