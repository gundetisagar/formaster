from dataclasses import dataclass
from typing import List

from gyaan.interactors.storages.dtos import DomainDTO, DomainStatsDTO, \
    UserDetailsDTO, DomainJoinRequestDTO, CompletePostDetailsDTO


@dataclass
class DomainDetailsDTO:
    domain: DomainDTO
    domain_stats: DomainStatsDTO
    domain_experts: List[UserDetailsDTO]
    join_requests: List[DomainJoinRequestDTO]
    requested_users: List[UserDetailsDTO]
    user_id: int
    is_user_domain_expert: bool


@dataclass
class DomainDetailsWithPostsDTO:
    post_details: CompletePostDetailsDTO
    domain_details: DomainDetailsDTO
