import pytest
from unittest.mock import create_autospec, patch
from reporting_portal.interactors.storages import (
    ObservationStorageInterface,
    CategoryStorageInterface
)
from reporting_portal.interactors.presenters import PresenterInterface
from reporting_portal.interactors.create_observation_interactor import \
    CreateObservationInteractor
from reporting_portal.exceptions.exceptions import (
    InvalidTitleContent,
    InvalidCategoryId,
    InvalidSubCategoryId,
    InvalidDescriptionContent,
    InvalidDescriptionLength
)
from django_swagger_utils.drf_server.exceptions import NotFound


def test_create_observation_with_title_empty_raises_exception():
    # Arrange
    user_id = 1
    invalid_title = ""
    category_id = 1
    sub_category_id = 1
    severty = "HIGH"
    description = "description"
    attachments = ["url_1"]

    observation_storage = create_autospec(ObservationStorageInterface)
    category_storage = create_autospec(CategoryStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateObservationInteractor(
        observation_storage=observation_storage,
        category_storage=category_storage
    )

    # Act
    interactor.create_obsevation_wrapper(
            user_id=user_id,
            title=invalid_title,
            category_id=category_id,
            sub_category_id=sub_category_id,
            severty=severty,
            description=description,
            attachments=attachments,
            presenter=presenter
        )

    # Assert
    presenter.raise_exception_for_invalid_title.assert_called_once()


def test_create_observation_with_title_content_more_than_max_limit_raises_exception():
    # Arrange
    user_id = 1
    invalid_title = "12345678910"
    category_id = 1
    sub_category_id = 1
    severty = "HIGH"
    description = "description"
    attachments = ["url_1"]

    observation_storage = create_autospec(ObservationStorageInterface)
    category_storage = create_autospec(CategoryStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateObservationInteractor(
        observation_storage=observation_storage,
        category_storage=category_storage
    )

    # Act
    interactor.create_obsevation_wrapper(
            user_id=user_id,
            title=invalid_title,
            category_id=category_id,
            sub_category_id=sub_category_id,
            severty=severty,
            description=description,
            attachments=attachments,
            presenter=presenter
        )

    # Assert
    presenter.raise_exception_for_invalid_title.assert_not_called()
    presenter.raise_exception_for_invalid_title_length.assert_called_once()


def test_create_observation_with_invalid_categoty_id_raises_exception():
    # Arrange
    user_id = 1
    title = "123456"
    invalid_category_id = 0
    sub_category_id = 1
    severty = "HIGH"
    description = "description"
    attachments = ["url_1"]

    observation_storage = create_autospec(ObservationStorageInterface)
    category_storage = create_autospec(CategoryStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateObservationInteractor(
        observation_storage=observation_storage,
        category_storage=category_storage
    )
    error = InvalidCategoryId(invalid_category_id)
    category_storage.is_valid_category.side_effect = error
    presenter.raise_exception_for_invalid_category_id.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_obsevation_wrapper(
            user_id=user_id,
            title=title,
            category_id=invalid_category_id,
            sub_category_id=sub_category_id,
            severty=severty,
            description=description,
            attachments=attachments,
            presenter=presenter
        )

    # Assert
    category_storage.is_valid_category.assert_called_once_with(
        category_id=invalid_category_id
    )
    presenter.raise_exception_for_invalid_category_id.\
        assert_called_once_with(error)


def test_create_observation_with_invalid_sub_categoty_id_raises_exception():
    # Arrange
    user_id = 1
    title = "123456"
    category_id = 1
    invalid_sub_category_id = 0
    severty = "HIGH"
    description = "description"
    attachments = ["url_1"]

    observation_storage = create_autospec(ObservationStorageInterface)
    category_storage = create_autospec(CategoryStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateObservationInteractor(
        observation_storage=observation_storage,
        category_storage=category_storage
    )

    error = InvalidSubCategoryId(invalid_sub_category_id)
    category_storage.is_valid_sub_category.side_effect = error
    presenter.raise_exception_for_invalid_sub_category_id.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_obsevation_wrapper(
            user_id=user_id,
            title=title,
            category_id=category_id,
            sub_category_id=invalid_sub_category_id,
            severty=severty,
            description=description,
            attachments=attachments,
            presenter=presenter
        )

    # Assert
    category_storage.is_valid_sub_category.assert_called_once_with(
        sub_category_id=invalid_sub_category_id
    )
    presenter.raise_exception_for_invalid_sub_category_id.\
        assert_called_once_with(error)


def test_create_observation_with_empty_description_raises_exception():
    # Arrange
    user_id = 1
    title = "12345"
    category_id = 1
    sub_category_id = 1
    severty = "HIGH"
    description = ""
    attachments = ["url_1"]

    observation_storage = create_autospec(ObservationStorageInterface)
    category_storage = create_autospec(CategoryStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateObservationInteractor(
        observation_storage=observation_storage,
        category_storage=category_storage
    )

    # Act
    interactor.create_obsevation_wrapper(
        user_id=user_id,
        title=title,
        category_id=category_id,
        sub_category_id=sub_category_id,
        severty=severty,
        description=description,
        attachments=attachments,
        presenter=presenter
    )

    # Assert
    presenter.raise_exception_for_invalid_description_content.assert_called_once()


def test_create_observation_with_description_lenth_more_than_max_limit_raises_exception():
    # Arrange
    user_id = 1
    title = "12345"
    category_id = 1
    sub_category_id = 1
    severty = "HIGH"
    description = "description length is more than max length"
    attachments = ["url_1"]

    observation_storage = create_autospec(ObservationStorageInterface)
    category_storage = create_autospec(CategoryStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateObservationInteractor(
        observation_storage=observation_storage,
        category_storage=category_storage
    )

    # Act
    interactor.create_obsevation_wrapper(
        user_id=user_id,
        title=title,
        category_id=category_id,
        sub_category_id=sub_category_id,
        severty=severty,
        description=description,
        attachments=attachments,
        presenter=presenter
    )

    # Assert
    presenter.raise_exception_for_invalid_description_content.assert_not_called()
    presenter.raise_exception_for_invalid_description_length.assert_called_once()
