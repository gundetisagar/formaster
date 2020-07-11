from typing import List
import abc
from formaster.dtos.dtos import FormTitleWithIdDto, FormDetailsDto

class FormStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_form(self, user_id: int,
                    form_title: str) -> FormDetailsDto:
        pass

    @abc.abstractmethod
    def get_forms(self, user_id: int) -> List[FormTitleWithIdDto]:
        pass

    @abc.abstractmethod
    def get_user_forms(self, user_id: int) -> List[FormTitleWithIdDto]:
        pass

    @abc.abstractmethod
    def validate_form_id(self, form_id: int) -> bool:
        pass

    @abc.abstractmethod
    def validate_is_user_creater_of_form(self, user_id: int,
                                         form_id: int) -> bool:
        pass

    @abc.abstractmethod
    def delete_form(self, form_id: int):
        pass

    @abc.abstractmethod
    def update_form_title(self, form_id: int,
                          new_form_title: str) -> FormTitleWithIdDto:
        pass
