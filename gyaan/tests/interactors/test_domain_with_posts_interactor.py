import pytest
from unittest.mock import create_autospec, patch
from gyaan.dtos.dtos import CompletePostDetailsDTO, DomainDetailsDTO, \
    DomainDetailsWithPostsDTO
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.domain_details_interactor import \
    DomainDetailsInteractor
from gyaan.interactors.domain_posts_interactor import \
    DomainPostsInteractor
from gyaan.interactors.domain_with_posts import DomainWithPostsInteractor
#from gyaan.interactors.storages.dtos import DomainDetailsDTO


@patch.object(DomainDetailsInteractor, "get_domain_details")
@patch.object(DomainPostsInteractor, "get_domain_posts")
def test_domain_with_posts_with_valid_data(
        get_domain_posts_mock,
        get_domain_details_mock,
        post_dtos,
        post_tag_details_dto,
        post_reaction_count_dto,
        post_comments_count_dto,
        comment_reaction_count_dto,
        comment_replies_count_dto,
        comment_dto,
        domain_stats_dto,
        domain_dto,
        users_dtos,
        requested_users_dto,
        domain_join_requests_dto):
    # Arrange
    
    domain_details_dto = DomainDetailsDTO(
        domain=domain_dto,
        domain_stats=domain_stats_dto,
        domain_experts=users_dtos,
        join_requests=domain_join_requests_dto,
        requested_users=requested_users_dto,
        user_id=1,
        is_user_domain_expert=True
    )
    
    completed_post_details_dto = CompletePostDetailsDTO(
        post_dtos=post_dtos,
        post_reaction_counts=post_reaction_count_dto,
        comment_reaction_counts=comment_reaction_count_dto,
        comment_counts=post_comments_count_dto,
        reply_counts=comment_replies_count_dto,
        comment_dtos=comment_dto,
        post_tag_ids=post_tag_details_dto.post_tag_ids,
        tags=post_tag_details_dto.tags,
        users_dtos=users_dtos
    )
    
    domain_details_with_posts_dto = DomainDetailsWithPostsDTO(
            domain_details=domain_details_dto,
            post_details=completed_post_details_dto
    )
    user_id = 1
    domain_id = 1
    offset = 0
    limit = 2
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainWithPostsInteractor(storage=storage)

    storage.is_valid_domain_id.return_value = True
    storage.is_user_following_domain.return_value = True
    get_domain_details_mock.return_value = domain_details_dto
    get_domain_posts_mock.return_value = completed_post_details_dto

    # Act
    interactor.get_domain_with_posts_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        offset=offset,
        limit=limit,
        presenter=presenter
    )

    # Assert
    presenter.raise_domain_does_not_exist_exception.assert_not_called()
    presenter.raise_user_not_domain_member_exception.assert_not_called()
    presenter.get_domain_with_posts_response.assert_called_once_with(
        domain_details_with_posts_dto
    )
