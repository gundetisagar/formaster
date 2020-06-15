from abc import abstractmethod
from typing import List
from reporting_portal.interactors.storages.dtos import CategoryDto


class PresenterInterface():

    @abstractmethod
    def get_categories_responses(self,
                                 list_of_categories_dto: List[CategoryDto]):
        pass

    @abstractmethod
    def raise_exception_for_invalid_title(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_title_length(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_category_id(self, error):
        pass

    @abstractmethod
    def raise_exception_for_invalid_sub_category_id(self, error):
        pass

    @abstractmethod
    def raise_exception_for_invalid_description_content(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_description_length(self):
        pass
