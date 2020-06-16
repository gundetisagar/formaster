from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.exceptions.exceptions import InvalidDate
from food_management.interactors.storages.storage_interface import \
    ItemDto
from typing import List


class CreateCustomPreferenceinteractor:
    def __init__(
            self,
            storage: StorageInterface):
        self.storage = storage

    def create_custom_preference_wrapper(self,
                                         user_id: int,
                                         date: str,
                                         meal_type: str,
                                         items_list: List[ItemDto],
                                         presenter: PresenterInterface):
        try:
            self.create_custom_preference(user_id=user_id,
                                          date=date,
                                          meal_type=meal_type,
                                          items_list=items_list)
        except InvalidDate as error:
            presenter.raise_exception_for_invalid_date(error)


    def create_custom_preference(self,
                                 user_id: int,
                                 date: str,
                                 meal_type: str,
                                 items_list: list):

        self.storage.is_valid_date(date=date)














































# invalid date
# invalid meal id
# validate item id
# validate  item quantity
# create or update
