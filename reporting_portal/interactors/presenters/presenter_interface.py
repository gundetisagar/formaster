from abc import abstractmethod


class PresenterInterface():

    @abstractmethod
    def get_categories_responses(self):
        pass
