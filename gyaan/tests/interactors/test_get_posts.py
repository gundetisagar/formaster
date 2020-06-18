import pytest
from unittest.mock import create_autospec, call
from gyaan.interactors.get_posts import \
    GetPosts
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.exceptions.exceptions import InvalidPostIds
from django_swagger_utils.drf_server.exceptions import BadRequest
from gyaan.interactors.storages.dtos import CompletePostDetailsDTO


class TestGetPosts:

    @staticmethod
    def test_get_post_with_invalid_post_ids_raises_exception():
        # Arrange
        post_ids = [1, 2, 2, 3, 3]
        unique_post_ids = [1,2,3]
        valid_post_ids = [1,2]
        invalid_post_ids = [3]
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPosts(storage=storage)

        storage.get_valid_post_ids.return_value = valid_post_ids
        presenter.raise_exception_for_invalid_post_ids.side_effect = BadRequest

        # Act
        with pytest.raises(BadRequest):
            interactor.get_posts_wrapper(
                post_ids=post_ids,
                presenter=presenter
            )
        
        # Assert
        storage.get_valid_post_ids.assert_called_once_with(unique_post_ids)
        error = presenter.raise_exception_for_invalid_post_ids.call_args.args[0]
        assert error.args[0] == invalid_post_ids


    @staticmethod
    def test_get_post_with_valid_post_details(
            post_dtos,
            post_tag_details_dto,
            post_reaction_count_dto,
            post_comments_count_dto,
            comment_reaction_count_dto,
            comment_replies_count_dto,
            comment_dto,
            users_dtos):
        # Arrange
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
        interactor = GetPosts(storage=storage)

        storage.get_valid_post_ids.return_value = post_ids
        storage.get_post_details.return_value = post_dtos
        storage.get_post_tags.return_value = post_tag_details_dto
        storage.get_post_reactions_count.return_value = post_reaction_count_dto
        storage.get_post_comments_count.return_value = post_comments_count_dto
        storage.get_latest_comment_ids.return_value = comment_ids
        storage.get_comment_reactions_count.return_value = comment_reaction_count_dto
        storage.get_comment_replies_count.return_value = comment_replies_count_dto
        storage.get_comment_details.return_value = comment_dto
        storage.get_users_details.return_value = users_dtos

        # Act
        completed_post_details_dict = interactor.get_posts_wrapper(
            post_ids=post_ids,
            presenter=presenter
        )

        # Assert
        storage.get_valid_post_ids.assert_called_once_with(post_ids)
        presenter.raise_exception_for_invalid_post_ids.assert_not_called()
        storage.get_post_details.assert_called_once_with(post_ids)
        storage.get_post_tags.assert_called_once_with(post_ids)
        storage.get_post_reactions_count.assert_called_once_with(
            post_ids=post_ids
        )
        storage.get_post_comments_count.assert_called_once_with(
            post_ids=post_ids
        )
        storage.get_comment_reactions_count.assert_called_once_with(
            comment_ids=comment_ids
        )
        storage.get_comment_replies_count.assert_called_once_with(
                comment_ids=comment_ids
        )
        storage.get_comment_details.assert_called_once_with(
            comment_ids=comment_ids
        )
        storage.get_users_details.assert_called_once_with(
            user_ids=user_ids
        )
        presenter.get_posts_response.assert_called_once_with(
            completed_post_details_dto=completed_post_details_dto
        )

