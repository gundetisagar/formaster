from typing import List
import abc
from formaster.dtos.dtos import (
    UserAuthTokensDto,
    UserDetailsDto,
    FormTitleWithIdDto,
    FormWithQuestionsDto,
    QuestionResponseDto,
    FormDetailsDto
)

class PresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abc.abstractmethod
    def user_login_response(self,
                            tokens_dto: UserAuthTokensDto,
                            is_admin: bool):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_user_id(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_user_is_not_admin(self):
        pass

    @abc.abstractmethod
    def get_user_profile_response(self, user_profile_dto: UserDetailsDto):
        pass

    @abc.abstractmethod
    def create_form_response(self, form_details_dto: FormDetailsDto):
        pass

    @abc.abstractmethod
    def get_forms_response(self,
                           form_title_with_id_dto: List[FormTitleWithIdDto]):
        pass

    @abc.abstractmethod
    def get_user_forms_response(
            self,
            form_title_with_id_dto: List[FormTitleWithIdDto]):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_question_type(self):
        pass

    @abc.abstractmethod
    def get_form_with_questions_response(
            self,
            form_with_list_of_questions_dto: List[FormWithQuestionsDto]):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_question_id(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_choice_id(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_form_id(self):
        pass

    @abc.abstractmethod
    def get_form_view_response(
            self,
            list_of_view_form_response_dto: List[QuestionResponseDto]):
        pass

    @abc.abstractmethod
    def raise_exception_for_user_is_not_creater_of_form(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_is_not_admin(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_user_cannot_update_form(self):
        pass

    @abc.abstractmethod
    def update_form_title_response(
        self, form_title_with_id_dto: FormTitleWithIdDto):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_response_form(self):
        pass
