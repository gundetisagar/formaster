from abc import abstractmethod


class ObservationStorageInterface:

    @abstractmethod
    def create_obsevation(
            self,
            user_id: int,
            title: str,
            category_id: int,
            sub_category_id: int,
            severty: str,
            description: str,
            attachments: list):
       pass
