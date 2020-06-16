from reporting_portal.interactors.storages import (
    ObservationStorageInterface,
    CategoryStorageInterface
)
from reporting_portal.interactors.presenters import \
    PresenterInterface
from reporting_portal.exceptions.exceptions import (
    InvalidTitleContent,
    InvalidDescriptionContent,
    InvalidCategoryId,
    InvalidSubCategoryId,
    InvalidTitleLength,
    InvalidDescriptionLength
)


class CreateObservationInteractor:

    def __init__(self, observation_storage: ObservationStorageInterface,
                 category_storage: CategoryStorageInterface):
        self.observation_storage = observation_storage
        self.category_storage = category_storage

    def create_obsevation_wrapper(self,
                                  user_id: int,
                                  title: str,
                                  category_id: int,
                                  sub_category_id: int,
                                  severty: str,
                                  description: str,
                                  attachments: list,
                                  presenter: PresenterInterface):

        try:
            self.create_obsevation(user_id=user_id,
                                   title=title,
                                   category_id=category_id,
                                   sub_category_id=sub_category_id,
                                   severty=severty,
                                   description=description,
                                   attachments=attachments)
        except InvalidTitleContent:
            presenter.raise_exception_for_invalid_title()
        except InvalidTitleLength:
            presenter.raise_exception_for_invalid_title_length()
        except InvalidCategoryId as error:
            presenter.raise_exception_for_invalid_category_id(error)
        except InvalidSubCategoryId as error:
            presenter.raise_exception_for_invalid_sub_category_id(error)
        except InvalidDescriptionContent:
            presenter.raise_exception_for_invalid_description_content()
        except InvalidDescriptionLength:
            presenter.raise_exception_for_invalid_description_length()


    def create_obsevation(self,
                          user_id: int,
                          title: str,
                          category_id: int,
                          sub_category_id: int,
                          severty: str,
                          description: str,
                          attachments: list):

        self._is_valid_title(title=title)

        self.category_storage.is_valid_category(category_id=category_id)

        self.category_storage.is_valid_sub_category(
            sub_category_id=sub_category_id
        )

        self._is_valid_description(description=description)

        self.observation_storage.create_obsevation(
            user_id=user_id,
            title=title,
            category_id=category_id,
            sub_category_id=sub_category_id,
            severty=severty,
            description=description,
            attachments=attachments)


    @staticmethod
    def _is_valid_title(title: str):
        if not title:
            raise InvalidTitleContent
        length_of_title = len(title)
        if length_of_title > 10:
            raise InvalidTitleLength


    @staticmethod
    def _is_valid_description(description: str):
        if not description:
            raise InvalidDescriptionContent
        length_of_description = len(description)
        print(length_of_description)
        if length_of_description > 15:
            raise InvalidDescriptionLength
