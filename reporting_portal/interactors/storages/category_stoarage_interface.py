from abc import abstractmethod

class CategoryStorageInterface():

    @abstractmethod
    def get_categories(self):
        pass
