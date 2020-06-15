from reporting_portal.interactors.presenters import PresenterInterface
from reporting_portal.interactors.storages import CategoryStorageInterface


class GetCategoriesInteractor:
    def __init__(self, category_storage: CategoryStorageInterface):
        self.category_storage = category_storage

    def get_categories_wrapper(self, presenter=PresenterInterface):
        list_of_categories_dto = self.get_categories()
        presenter.get_categories_responses(list_of_categories_dto)

    def get_categories(self):
        list_of_categories_dto = self.category_storage.get_categories()
        return list_of_categories_dto
