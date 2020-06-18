import pytest
from unittest.mock import create_autospec, call
from gyaan.interactors.domain_details_interactor import \
    DomainDetailsInteractor
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.exceptions.exceptions import (
    DomainDoesNotExist,
    UserNotDomainMember
)
from django_swagger_utils.drf_server.exceptions import NotFound
from gyaan.dtos.dtos import DomainDetailsDTO


class TestDomainDetailsInteractor:

    @staticmethod
    def test_get_domain_details_with_invalid_domain_id_raises_exception():
        # Arrange
        user_id = 1
        domain_id = 1
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = DomainDetailsInteractor(storage=storage)

        storage.get_domain.side_effect = DomainDoesNotExist
        presenter.raise_domain_does_not_exist_exception.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.get_domain_details_wrapper(
                user_id=user_id,
                domain_id=domain_id,
                presenter=presenter
            )

        # Assert
        storage.get_domain.assert_called_once_with(domain_id=domain_id)
        presenter.raise_domain_does_not_exist_exception.assert_called_once()

    @staticmethod
    def test_get_domain_details_with_user_not_following_domain_raises_exception():
        # Arrange
        user_id = 1
        domain_id = 1
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = DomainDetailsInteractor(storage=storage)

        error = UserNotDomainMember(domain_id)
        print(error)
        storage.is_user_following_domain.return_value = False
        presenter.raise_user_not_domain_member_exception.side_effect = \
            NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.get_domain_details_wrapper(
                user_id=user_id,
                domain_id=domain_id,
                presenter=presenter
            )

        # Assert
        storage.is_user_following_domain.assert_called_once_with(
            user_id, domain_id)
        error = presenter.raise_user_not_domain_member_exception.call_args.args[0]
        assert error.args[0] == user_id

    @staticmethod
    def test_get_domain_details_with_domain_expert(
            domain_stats_dto,
            domain_dto,
            users_dtos,
            requested_users_dto,
            domain_join_requests_dto):
        # Arrange
        user_id = 1
        domain_id =1
        domain_expert_ids = [1, 2]
        user_ids = [3, 4]
        domain_details_dto = DomainDetailsDTO(
            domain=domain_dto,
            domain_stats=domain_stats_dto,
            domain_experts=users_dtos,
            join_requests=domain_join_requests_dto,
            requested_users=requested_users_dto,
            user_id=1,
            is_user_domain_expert=True
        )
        # expected_dict = {
        #     "domain_id": 1,
        #     "name": "domain name"
        # }
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = DomainDetailsInteractor(storage=storage)

        storage.get_domain.return_value = domain_dto
        storage.is_user_following_domain.return_value = True
        storage.get_domain_stats.return_value = domain_stats_dto
        storage.get_domain_expert_ids.return_value = domain_expert_ids
        storage.get_users_details.side_effect = [users_dtos, requested_users_dto]
        storage.is_user_domain_expert.return_value = True
        storage.get_domain_join_requests.return_value = domain_join_requests_dto

        # presenter.get_domain_details_response.return_value = expected_dict

        # Act
        
        domain_details_dict = interactor.get_domain_details_wrapper(
            user_id, domain_id, presenter
        )

        # Assert
        print(domain_details_dict)
        #assert domain_details_dict == expected_dict
        storage.get_domain.assert_called_once_with(domain_id)
        storage.is_user_following_domain.assert_called_once_with(
            user_id, domain_id
        )
        storage.get_domain_stats.assert_called_once_with(domain_id)
        storage.get_domain_expert_ids.assert_called_once_with(domain_id)
        storage.get_users_details.assert_has_calls([call(domain_expert_ids), call(user_ids)])
        storage.is_user_domain_expert.assert_called_once_with(user_id, domain_id)
        storage.get_domain_join_requests.assert_called_once_with(domain_id)
        presenter.get_domain_details_response.assert_called_once_with(domain_details_dto)


    @staticmethod
    def test_get_domain_details_with_normal_user_expert(
            domain_stats_dto,
            domain_dto,
            users_dtos):
            # requested_users_dto,
            # domain_join_requests_dto):
        # Arrange
        user_id = 1
        domain_id =1
        domain_expert_ids = [1, 2]
        user_ids = []
        domain_details_dto = DomainDetailsDTO(
            domain=domain_dto,
            domain_stats=domain_stats_dto,
            domain_experts=users_dtos,
            join_requests=[],
            requested_users=[],
            user_id=1,
            is_user_domain_expert=False
        )
        # expected_dict = {
        #     "domain_id": 1,
        #     "name": "domain name"
        # }
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = DomainDetailsInteractor(storage=storage)

        storage.get_domain.return_value = domain_dto
        storage.is_user_following_domain.return_value = True
        storage.get_domain_stats.return_value = domain_stats_dto
        storage.get_domain_expert_ids.return_value = domain_expert_ids
        storage.get_users_details.return_value = users_dtos
        storage.is_user_domain_expert.return_value = False
        storage.get_domain_join_requests.return_value = user_ids

        # presenter.get_domain_details_response.return_value = expected_dict

        # Act
        
        domain_details_dict = interactor.get_domain_details_wrapper(
            user_id, domain_id, presenter
        )

        # Assert
        print(domain_details_dict)
        #assert domain_details_dict == expected_dict
        storage.get_domain.assert_called_once_with(domain_id)
        storage.is_user_following_domain.assert_called_once_with(
            user_id, domain_id
        )
        storage.get_domain_stats.assert_called_once_with(domain_id)
        storage.get_domain_expert_ids.assert_called_once_with(domain_id)
        storage.get_users_details.assert_called_once_with(domain_expert_ids)
        storage.is_user_domain_expert.assert_called_once_with(user_id, domain_id)
        storage.get_domain_join_requests.assert_not_called()
        presenter.get_domain_details_response.assert_called_once_with(domain_details_dto)
