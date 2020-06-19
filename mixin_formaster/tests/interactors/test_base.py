import pytest
from unittest.mock import create_autospec
from mixin_formaster.interactors.storages.storage_interface import \
    StorageInterface
from mixin_formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from mixin_formaster.interactors.base import \
    BaseSubmitFormResponseInteractor
from mixin_formaster.interactors.mcq_question import \
    MCQQuestionSubmitFormResponseInteractor
from mixin_formaster.exceptions.exceptions import FormDoesNotExist, \
    FormClosed, QuestionDoesNotBelongToForm, InvalidUserResponseSubmit
from django_swagger_utils.drf_server.exceptions import NotFound


class TestBaseSubmitFormResponseInteractor:

    @staticmethod
    def test_with_invalid_form_id():
        # Arrange
        user_id = 1
        form_id = 1
        question_id = 1

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = BaseSubmitFormResponseInteractor(
            storage=storage,
            question_id=question_id,
            form_id=form_id,
            user_id=user_id
        )

        storage.is_valid_form_id.side_effect = FormDoesNotExist
        presenter.raise_form_does_not_exist_exception.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.submit_form_response_wrapper(
                presenter=presenter
            )

        # Assert
        storage.is_valid_form_id.assert_called_once_with(form_id)
        presenter.raise_form_does_not_exist_exception.assert_called_once()

    @staticmethod
    def test_with_valid_form_id():
        # Arrange
        user_id = 1
        form_id = 1
        question_id = 1

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = BaseSubmitFormResponseInteractor(
            storage=storage,
            question_id=question_id,
            form_id=form_id,
            user_id=user_id
        )

        storage.is_valid_form_id.return_value = True

        # Act
        interactor.submit_form_response_wrapper(
            presenter=presenter
        )

        # Assert
        storage.is_valid_form_id.assert_called_once_with(form_id)
        presenter.raise_form_does_not_exist_exception.assert_not_called()

    @staticmethod
    def test_with_invalid_question_id_with_form():
        # Arrange
        user_id = 1
        form_id = 1
        question_id = 1

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = BaseSubmitFormResponseInteractor(
            storage=storage,
            question_id=question_id,
            form_id=form_id,
            user_id=user_id
        )

        storage.validate_question_id_with_form.side_effect = \
            QuestionDoesNotBelongToForm
        presenter.raise_question_does_not_belong_to_form_exception.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.submit_form_response_wrapper(
                presenter=presenter
            )

        # Assert
        storage.validate_question_id_with_form.assert_called_once_with(
            question_id, form_id
        )
        presenter.raise_question_does_not_belong_to_form_exception.assert_called_once()

    @staticmethod
    def test_with_form_closed_exception():
        # Arrange
        user_id = 1
        form_id = 1
        question_id = 1

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = BaseSubmitFormResponseInteractor(
            storage=storage,
            question_id=question_id,
            form_id=form_id,
            user_id=user_id
        )

        storage.get_form.side_effect = FormClosed
        presenter.raise_form_closed_exception.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.submit_form_response_wrapper(
                presenter=presenter
            )

        # Assert
        storage.get_form.assert_called_once_with(form_id)
        presenter.raise_form_closed_exception.assert_called_once()

class TestMCQQuestionSubmitFormResponseInteractor:

    @staticmethod
    def test_invalid_user_response():
        # Arrange
        user_id = 1
        form_id = 1
        question_id = 1
        user_submitted_option_id = 1
        option_ids = [2, 3]

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = MCQQuestionSubmitFormResponseInteractor(
            storage=storage,
            question_id=question_id,
            form_id=form_id,
            user_id=user_id,
            user_submitted_option_id=user_submitted_option_id
        )

        storage.get_option_ids_for_question.return_value = option_ids
        presenter.raise_invalid_user_response_submitted.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.submit_form_response_wrapper(
                presenter=presenter
            )

        # Assert
        storage.get_option_ids_for_question.assert_called_once_with(question_id)
        presenter.raise_invalid_user_response_submitted.assert_called_once()


    @staticmethod
    def test_create_user_response():
        # Arrange
        user_id = 1
        form_id = 1
        question_id = 1
        user_submitted_option_id = 1
        option_ids = [1, 3]
        response_id = 1

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = MCQQuestionSubmitFormResponseInteractor(
            storage=storage,
            question_id=question_id,
            form_id=form_id,
            user_id=user_id,
            user_submitted_option_id=user_submitted_option_id
        )

        storage.get_option_ids_for_question.return_value = option_ids
        storage.validate_question_id.return_value = True
        storage.create_user_mcq_response.return_value = response_id
        presenter.submit_form_response_return.return_value = response_id

        # Act
        user_response_id =  interactor.submit_form_response_wrapper(
                presenter=presenter
            )

        # Assert
        storage.get_option_ids_for_question.assert_called_once_with(question_id)
        storage.create_user_mcq_response.assert_called_once_with(
            user_id, form_id, user_submitted_option_id
        )
        assert response_id == user_response_id
