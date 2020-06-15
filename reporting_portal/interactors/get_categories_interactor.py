from reporting_portal.interactors.presenters import PresenterInterface
from reporting_portal.interactors.storages import CategoryStorageInterface


class GetCategoriesInteractor:
    def __init__(self, category_storage: CategoryStorageInterface,
                 presenter: PresenterInterface):
        self.category_storage = category_storage
        self.presenter = presenter

    def get_categories(self):
        list_of_categories_dto = self.category_storage.get_categories()
        list_of_categories_dict = self.presenter.get_categories_responses(
            list_of_categories_dto
        )
        return list_of_categories_dict
