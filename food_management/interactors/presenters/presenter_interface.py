from abc import abstractmethod


class PresenterInterface:

    @abstractmethod
    def raise_exception_for_invalid_date(self, error):
        pass
