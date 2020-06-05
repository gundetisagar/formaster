from typing import List
from abc import abstractmethod
from formaster.dtos.dtos import FormTitleWithIdDto

class FormStorageInterface:

    @abstractmethod
    def add_form_title(self, user_id: int,
                       form_title: str) -> FormTitleWithIdDto:
        pass

    @abstractmethod
    def get_forms(self, user_id: int) -> List[FormTitleWithIdDto]:
        pass

    @abstractmethod
    def get_user_forms(self, user_id: int) -> List[FormTitleWithIdDto]:
        pass

    @abstractmethod
    def validate_form_id(self, form_id: int) -> bool:
        pass

    @abstractmethod
    def validate_is_user_creater_of_form(self, user_id: int,
                                         form_id: int) -> bool:
        pass

    @abstractmethod
    def delete_form(self, form_id: int):
        pass

    @abstractmethod
    def update_form_title(self, form_id: int,
                          new_form_title: str) -> FormTitleWithIdDto:
        pass
