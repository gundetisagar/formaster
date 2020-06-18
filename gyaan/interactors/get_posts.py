from typing import List
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.exceptions.exceptions import InvalidPostIds
from gyaan.interactors.storages.dtos import CompletePostDetailsDTO



class GetPosts:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_posts_wrapper(self, post_ids: List[int],
                          presenter: PresenterInterface):
        try:
            return self._prepare_posts_response(
                post_ids=post_ids,
                presenter=presenter
            )
        except InvalidPostIds as error:
            print(error)
            presenter.raise_exception_for_invalid_post_ids(error)

    def _prepare_posts_response(self, post_ids: List[int],
                                presenter: PresenterInterface):
        completed_post_details_dto = self.get_posts(post_ids=post_ids)
        completed_post_details_dict = presenter.get_posts_response(
            completed_post_details_dto
        )
        return completed_post_details_dict

    def get_posts(self, post_ids: List[int]):
        unique_post_ids = self._get_unique_post_ids(post_ids)

        self._validate_post_ids(post_ids=unique_post_ids)

        list_of_post_dtos = self.storage.get_post_details(
            post_ids=post_ids
        )

        post_tag_details_dto = self.storage.get_post_tags(post_ids=post_ids)

        list_of_post_reaction_counts_dtos = \
            self.storage.get_post_reactions_count(post_ids=post_ids)

        list_of_posts_comment_counts_dtos = \
            self.storage.get_post_comments_count(post_ids=post_ids)

        list_of_comment_ids = self._get_latest_comment_ids(post_ids=post_ids)

        list_of_comment_reaction_counts_dtos = \
            self.storage.get_comment_reactions_count(
                comment_ids=list_of_comment_ids
        )

        list_of_comment_replies_counts_dtos = \
            self.storage.get_comment_replies_count(
                comment_ids=list_of_comment_ids
        )

        list_of_comment_dtos = self.storage.get_comment_details(
            comment_ids=list_of_comment_ids
        )

        user_ids = [
            post_dto.posted_by_id
            for post_dto in list_of_post_dtos
        ]

        user_ids += [
            comment_dto.commented_by_id
            for comment_dto in list_of_comment_dtos
        ]
        unique_user_ids = self._get_unique_post_ids(user_ids)

        list_of_user_dtos = self.storage.get_users_details(
            user_ids=unique_user_ids
        )

        return CompletePostDetailsDTO(
            post_dtos=list_of_post_dtos,
            post_reaction_counts=list_of_post_reaction_counts_dtos,
            comment_reaction_counts=list_of_comment_reaction_counts_dtos,
            comment_counts=list_of_posts_comment_counts_dtos,
            reply_counts=list_of_comment_replies_counts_dtos,
            comment_dtos=list_of_comment_dtos,
            post_tag_ids=post_tag_details_dto.post_tag_ids,
            tags=post_tag_details_dto.tags,
            users_dtos=list_of_user_dtos
        )


    def _get_latest_comment_ids(self, post_ids):
        list_of_comment_ids = []
        for post_id in post_ids:
            list_of_comment_ids += self.storage.get_latest_comment_ids(
                post_id=post_id, no_of_comments=2
            )
        return list_of_comment_ids


    @staticmethod
    def _get_unique_post_ids(post_ids):
        unique_post_ids = list(set(post_ids))
        return unique_post_ids

    def _validate_post_ids(self, post_ids):
        valid_post_ids = self.storage.get_valid_post_ids(post_ids)

        invalid_post_ids = [
            post_id
            for post_id in post_ids if post_id not in valid_post_ids
        ]

        if invalid_post_ids:
            raise InvalidPostIds(invalid_post_ids)
