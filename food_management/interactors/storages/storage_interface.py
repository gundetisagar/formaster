from abc import abstractmethod
class StorageInterface:

    @abstractmethod
    def is_valid_date(self, date: str):
        pass










from dataclasses import dataclass

@dataclass()
class ItemDto:
    item_id: int
    item_quantity: int
