import pytest
from unittest.mock import create_autospec, patch
from gyaan.interactors.get_posts import GetPosts
from gyaan.interactors.domain_posts_interactor import \
    DomainPostsInteractor
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.interactors.storages.dtos import CompletePostDetailsDTO



class TestDomainPosts:

    @staticmethod
    @patch.object(GetPosts, "get_posts")
    def test_domain_posts_with_valid_data(
            get_posts_mock,
            post_dtos,
            post_tag_details_dto,
            post_reaction_count_dto,
            post_comments_count_dto,
            comment_reaction_count_dto,
            comment_replies_count_dto,
            comment_dto,
            users_dtos):
        # Arrange
        user_id = 1
        domain_id = 1
        offset = 0
        limit = 5
        post_ids = [1]
        comment_ids = [1]
        user_ids = [1]

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

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DomainPostsInteractor(storage=storage)

        storage.is_valid_domain_id.return_value = True
        storage.is_user_following_domain.return_value = True
        get_posts_mock.return_value = completed_post_details_dto

        # Act
        domain_posts_detail_dict = interactor.get_domain_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

        # Assert
        storage.is_valid_domain_id.assert_called_once_with(domain_id)
        presenter.raise_domain_does_not_exist_exception.assert_not_called()
        storage.get_domain_post_ids.assert_called_once_with(domain_id, offset, limit)
        storage.is_user_following_domain.assert_called_once_with(
            user_id=user_id,
            domain_id=domain_id
        )
        presenter.raise_user_not_domain_member_exception.assert_not_called
        presenter.get_domain_posts_response.assert_called_once_with(
            completed_post_details_dto
        )
