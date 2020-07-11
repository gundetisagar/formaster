import pytest
from formaster.interactors.form_interactor import FormInteractor
from freezegun import freeze_time


class TestCreateFormInteractor:

	@pytest.fixture
	def storage_mock(self):
		from formaster.interactors.storages.form_storage_interface import \
			FormStorageInterface
		from mock import create_autospec
		storage = create_autospec(FormStorageInterface)
		return storage

	@pytest.fixture
	def presenter_mock(self):
		from formaster.interactors.presenters.presenter_interface import \
			PresenterInterface
		from mock import create_autospec
		storage = create_autospec(PresenterInterface)
		return storage

	@staticmethod
	@freeze_time("2020-01-1 05:21:34")
	def test_with_invalid_user_id_raises_exception(mocker, storage_mock,
												   presenter_mock):
		# Arrange
		user_id = 0
		form_title = "form_title_1"
		from formaster_auth.exceptions.exceptions import InvalidUserId
		from formaster.tests.common_fixtures.adapters.auth_service import \
			invalid_user_id_mock

		invalid_user_id_mock(mocker, user_id)
		from django_swagger_utils.drf_server.exceptions import NotFound
		presenter_mock.raise_exception_for_invalid_user_id.side_effect = NotFound

		interactor = FormInteractor(form_storage=storage_mock)

		# Act
		with pytest.raises(NotFound):
			interactor.create_form_wrapper(user_id=user_id,
										   form_title=form_title,
										   presenter=presenter_mock)

		# Assert
		presenter_mock.raise_exception_for_invalid_user_id.assert_called_once()

	@staticmethod
	@freeze_time("2020-01-1 05:21:34")
	def test_with_user_is_not_admin_raises_exception(mocker, storage_mock,
													 presenter_mock):
		# Arrange
		user_id = 1
		form_title = "form_title_1"
		from formaster.tests.common_fixtures.adapters.auth_service import \
			invalid_is_admin_mock, is_valid_user_mock

		is_valid_user_mock(mocker, user_id)
		invalid_is_admin_mock(mocker, user_id)
		from django_swagger_utils.drf_server.exceptions import NotFound
		presenter_mock.raise_exception_for_user_is_not_admin.side_effect = NotFound

		interactor = FormInteractor(form_storage=storage_mock)

		# Act
		with pytest.raises(NotFound):
			interactor.create_form_wrapper(user_id=user_id,
										   form_title=form_title,
										   presenter=presenter_mock)

		# Assert
		presenter_mock.raise_exception_for_user_is_not_admin.assert_called_once()

	@staticmethod
	@freeze_time("2020-01-1 05:21:34")
	def test_with_valid_details_returns_form_details(mocker, storage_mock,
													 presenter_mock):
		# Arrange
		user_id = 1
		form_id = 1
		form_title = "form_title_1"
		from formaster.dtos.dtos import FormDetailsDto
		expected_form_details_dto = FormDetailsDto(
			form_title=form_title,
			form_id=form_id
		)
		expected_form_details_dict = {
			"form_title": "form_title_1",
			"form_id": 1
		}
		from formaster.tests.common_fixtures.adapters.auth_service import \
			is_valid_user_mock, is_valid_admin_mock

		is_valid_user_mock(mocker, user_id)
		is_valid_admin_mock(mocker, user_id)

		storage_mock.create_form.return_value = expected_form_details_dto
		presenter_mock.create_form_response.return_value = \
			expected_form_details_dict

		interactor = FormInteractor(form_storage=storage_mock)

		# Act
		form_details_dict = interactor.create_form_wrapper(
			user_id=user_id,
			form_title=form_title,
			presenter=presenter_mock
		)

		# Assert
		storage_mock.create_form.assert_called_once_with(
			user_id=user_id,
			form_title=form_title
		)
		assert expected_form_details_dict == form_details_dict
		presenter_mock.create_form_response.assert_called_once_with(
			form_details_dto=expected_form_details_dto
		)
