import pytest
from unittest.mock import create_autospec
from formaster.interactors.delete_question_interactor import \
    DeleteQuestionInteractor
from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.user_storage_interface import \
    UserStorageInterface
from formaster.interactors.storages.question_storage_interface import \
    QuestionStorageInterface
from formaster.exceptions.exceptions import (
    UserIsNotAdmin,
    InvalidFormId,
    InvalidQuestionId,
    UserIsNotCreaterOfForm
)


def test_delete_question_with_invalid_question_id():
    # Arrange
    user_id = 1
    form_id = 2
    question_id = 0
    form_storage = create_autospec(FormStorageInterface)
    user_storage = create_autospec(UserStorageInterface)
    questions_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(PresenterInterface)

    questions_storage.validate_question_id.side_effect = InvalidQuestionId

    interactor = DeleteQuestionInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        questions_storage=questions_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_question(
        user_id=user_id,
        form_id=form_id,
        question_id=question_id
    )

    # Assert
    questions_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question_id.\
        assert_called_once_with()
    user_storage.validate_is_admin.assert_not_called()
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_not_called()
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    questions_storage.delete_question.assert_not_called()

def test_delete_question_with_valid_question_id():
    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    form_storage = create_autospec(FormStorageInterface)
    user_storage = create_autospec(UserStorageInterface)
    questions_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(PresenterInterface)

    questions_storage.validate_question_id.return_value = True

    interactor = DeleteQuestionInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        questions_storage=questions_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_question(
        user_id=user_id,
        form_id=form_id,
        question_id=question_id
    )

    # Assert
    questions_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question_id.assert_not_called()
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(form_id=form_id)
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    questions_storage.delete_question.assert_called_once_with(
        question_id=question_id
    )



def test_delete_question_with_user_is_not_admin():
    # Arrange
    user_id = 1
    form_id = 2
    question_id = 1
    form_storage = create_autospec(FormStorageInterface)
    user_storage = create_autospec(UserStorageInterface)
    questions_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(PresenterInterface)

    questions_storage.validate_question_id.return_value = True
    user_storage.validate_is_admin.side_effect = UserIsNotAdmin

    interactor = DeleteQuestionInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        questions_storage=questions_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_question(
        user_id=user_id,
        form_id=form_id,
        question_id=question_id
    )

    # Assert
    questions_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question_id.assert_not_called()
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_called_once()
    form_storage.validate_form_id.assert_not_called()
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    questions_storage.delete_question.assert_not_called()


def test_delete_question_with_user_is_admin():
    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    form_storage = create_autospec(FormStorageInterface)
    user_storage = create_autospec(UserStorageInterface)
    questions_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(PresenterInterface)

    questions_storage.validate_question_id.return_value = True
    user_storage.validate_is_admin.return_value = True

    interactor = DeleteQuestionInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        questions_storage=questions_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_question(
        user_id=user_id,
        form_id=form_id,
        question_id=question_id
    )

    # Assert
    questions_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question_id.assert_not_called()
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(form_id=form_id)
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    questions_storage.delete_question.assert_called_once_with(
        question_id=question_id
    )


def test_delete_question_with_invalid_form_id():
    # Arrange
    user_id = 1
    invalid_form_id = 0
    question_id = 1
    form_storage = create_autospec(FormStorageInterface)
    user_storage = create_autospec(UserStorageInterface)
    questions_storage = create_autospec(QuestionStorageInterface)
    presenter = create_autospec(PresenterInterface)

    questions_storage.validate_question_id.return_value = True
    user_storage.validate_is_admin.return_value = True
    form_storage.validate_form_id.side_effect = InvalidFormId

    interactor = DeleteQuestionInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        questions_storage=questions_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_question(
        user_id=user_id,
        form_id=invalid_form_id,
        question_id=question_id
    )

    # Assert
    questions_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question_id.assert_not_called()
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(
        form_id=invalid_form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_called_once()
    questions_storage.delete_question.assert_not_called()


def test_delete_question_with_valid_form_id():
    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)
    questions_storage = create_autospec(QuestionStorageInterface)
    user_storage = create_autospec(UserStorageInterface)

    questions_storage.validate_question_id.return_value = True
    user_storage.validate_is_admin.return_value = True
    form_storage.validate_form_id.return_value = True


    interactor = DeleteQuestionInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        questions_storage=questions_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_question(
        user_id=user_id,
        form_id=form_id,
        question_id=question_id
    )

    # Assert
    questions_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(
        form_id=form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    form_storage.validate_is_user_creater_of_form.assert_called_once_with(
        user_id=user_id, form_id=form_id
    )
    presenter.raise_exception_for_user_cannot_delete_form.assert_not_called()
    questions_storage.delete_question.assert_called_once_with(
        question_id=question_id
    )


def test_delete_question_with_user_not_creater_of_form():
    # Arrange
    user_id = 1
    form_id = 2
    question_id = 1
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)
    questions_storage = create_autospec(QuestionStorageInterface)
    user_storage = create_autospec(UserStorageInterface)

    questions_storage.validate_question_id.return_value = True
    user_storage.validate_is_admin.return_value = True
    form_storage.validate_form_id.return_value = True
    form_storage.validate_is_user_creater_of_form.side_effect = \
        UserIsNotCreaterOfForm


    interactor = DeleteQuestionInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        questions_storage=questions_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_question(
        user_id=user_id,
        form_id=form_id,
        question_id=question_id
    )

    # Assert
    questions_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question_id.assert_not_called()
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(
        form_id=form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    form_storage.validate_is_user_creater_of_form.assert_called_once_with(
        user_id=user_id, form_id=form_id
    )
    presenter.raise_exception_for_user_cannot_delete_form.assert_called_once()
    questions_storage.delete_question.assert_not_called()


def test_delete_form_with_user_is_creater_of_form():
    # Arrange
    user_id = 1
    question_id = 1
    form_id = 1
    form_storage = create_autospec(FormStorageInterface)
    presenter = create_autospec(PresenterInterface)
    questions_storage = create_autospec(QuestionStorageInterface)
    user_storage = create_autospec(UserStorageInterface)

    questions_storage.validate_question_id.return_value = True
    user_storage.validate_is_admin.return_value = True
    form_storage.validate_form_id.return_value = True
    form_storage.validate_is_user_creater_of_form.return_value = True

    interactor = DeleteQuestionInteractor(
        form_storage=form_storage,
        user_storage=user_storage,
        questions_storage=questions_storage,
        presenter=presenter
    )

    # Act
    interactor.delete_question(
        user_id=user_id,
        form_id=form_id,
        question_id=question_id
    )

    # Assert
    questions_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question_id.assert_not_called()
    user_storage.validate_is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_is_not_admin.assert_not_called()
    form_storage.validate_form_id.assert_called_once_with(
        form_id=form_id
    )
    presenter.raise_exception_for_invalid_form_id.assert_not_called()
    form_storage.validate_is_user_creater_of_form.assert_called_once_with(
        user_id=user_id, form_id=form_id
    )
    presenter.raise_exception_for_user_cannot_delete_form.assert_not_called()
    questions_storage.delete_question.assert_called_once_with(
        question_id=question_id
    )
