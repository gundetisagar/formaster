from formaster.interactors.storages.choice_storage_interface import \
    ChoiceStorageInterface
from formaster.models.choices import Choices
from formaster.exceptions.exceptions import InvalidChoiceId


class ChoiceStorageImplementation(ChoiceStorageInterface):

    def validate_choice_id(self, choice_id: int) -> bool:
        try:
            Choices.objects.get(id=choice_id)
        except Choices.DoesNotExist:
            raise InvalidChoiceId
        return True
