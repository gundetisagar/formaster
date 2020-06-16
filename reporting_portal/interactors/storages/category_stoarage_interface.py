from abc import abstractmethod
from typing import List
from reporting_portal.interactors.storages.dtos import CategoryDto


class CategoryStorageInterface():

    @abstractmethod
    def get_categories(self) -> List[CategoryDto]:
        pass

    @abstractmethod
    def is_valid_category(self, category_id: int):
        pass

    @abstractmethod
    def is_valid_sub_category(self, sub_category_id: int):
        pass

    @abstractmethod
    def get_user_observations(self):
        pass
