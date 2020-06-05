from abc import abstractmethod


class ChoiceStorageInterface:
    @abstractmethod
    def validate_choice_id(self, choice_id: int) -> bool:
        pass

