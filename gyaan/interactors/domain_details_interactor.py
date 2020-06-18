from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.exceptions.exceptions import (
    DomainDoesNotExist,
    UserNotDomainMember
)
from gyaan.dtos.dtos import DomainDetailsDTO


class DomainDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_details_wrapper(self, user_id: int, domain_id: int,
                                   presenter: PresenterInterface) -> dict:
        from gyaan.exceptions.exceptions import DomainDoesNotExist
        try:
            return self._get_domain_details_response(
                user_id=user_id, domain_id=domain_id,
                presenter=presenter
            )
        except DomainDoesNotExist:
            presenter.raise_domain_does_not_exist_exception()
        except UserNotDomainMember as error:
            presenter.raise_user_not_domain_member_exception(error)


    def _get_domain_details_response(self, user_id: int, domain_id: int,
                                     presenter: PresenterInterface):
        domain_details_dto = self.get_domain_details(user_id, domain_id)
        domain_details_dict = presenter.get_domain_details_response(
            domain_details_dto
            )
        return domain_details_dict

    def get_domain_details(self, user_id: int, domain_id: int):
        domain_dto = self.storage.get_domain(domain_id)

        is_user_following = self.storage.is_user_following_domain(
            user_id, domain_id)

        if not is_user_following:
            raise UserNotDomainMember(user_id)

        domain_stats_dto = self.storage.get_domain_stats(domain_id)
        domain_expert_ids = self.storage.get_domain_expert_ids(domain_id)
        domain_experts_dto = self.storage.get_users_details(domain_expert_ids)

        is_user_domain_expert, domain_join_requests, requested_user_dtos = \
            self._get_domain_expert_details(
                user_id=user_id, domain_id=domain_id
            )
        response = DomainDetailsDTO(
            domain=domain_dto,
            domain_stats=domain_stats_dto,
            domain_experts=domain_experts_dto,
            user_id=user_id,
            is_user_domain_expert=is_user_domain_expert,
            join_requests=domain_join_requests,
            requested_users=requested_user_dtos
        )
        return response

    def _get_domain_expert_details(self, user_id: int, domain_id: int):
        is_user_domain_expert = self.storage.is_user_domain_expert(
            user_id, domain_id
        )
        domain_join_requests = []
        requested_user_dtos = []

        if is_user_domain_expert:
            domain_join_requests = self.storage.get_domain_join_requests(
                domain_id
            )
        if domain_join_requests:
            requested_user_dtos = self.storage.get_users_details(
                [dto.user_id for dto in domain_join_requests]
            )
        return is_user_domain_expert, domain_join_requests, requested_user_dtos
