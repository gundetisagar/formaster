from typing import List
from abc import abstractmethod
from formaster.dtos.dtos import (
    UserAuthTokensDto,
    UserDetailsDto,
    FormTitleWithIdDto,
    FormWithQuestionsDto,
    QuestionResponseDto,
    FormDetailsDto
)

class PresenterInterface():

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def user_login_response(self,
                            tokens_dto: UserAuthTokensDto,
                            is_admin: bool):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user_id(self):
        pass

    @abstractmethod
    def raise_exception_for_user_is_not_admin(self):
        pass

    @abstractmethod
    def get_user_profile_response(self, user_profile_dto: UserDetailsDto):
        pass

    @abstractmethod
    def add_form_title_response(self, form_details_dto: FormDetailsDto):
        pass

    @abstractmethod
    def get_forms_response(self,
                           form_title_with_id_dto: List[FormTitleWithIdDto]):
        pass

    @abstractmethod
    def get_user_forms_response(
            self,
            form_title_with_id_dto: List[FormTitleWithIdDto]):
        pass

    @abstractmethod
    def raise_exception_for_invalid_question_type(self):
        pass

    @abstractmethod
    def get_form_with_questions_response(
            self,
            form_with_list_of_questions_dto: List[FormWithQuestionsDto]):
        pass

    @abstractmethod
    def raise_exception_for_invalid_question_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_choice_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_form_id(self):
        pass

    @abstractmethod
    def get_form_view_response(
            self,
            list_of_view_form_response_dto: List[QuestionResponseDto]):
        pass

    @abstractmethod
    def raise_exception_for_user_is_not_creater_of_form(self):
        pass

    @abstractmethod
    def raise_exception_for_is_not_admin(self):
        pass

    @abstractmethod
    def raise_exception_for_user_cannot_update_form(self):
        pass

    @abstractmethod
    def update_form_title_response(
        self, form_title_with_id_dto: FormTitleWithIdDto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_response_form(self):
        pass
