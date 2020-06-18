import pytest
import datetime
from gyaan.interactors.storages.dtos import (
    DomainStatsDTO, DomainDTO, UserDetailsDTO, DomainJoinRequestDTO, PostDTO,
    TagDTO, PostTagDTO, PostTagDetailsDTO, PostReactionsCountDTO,
    PostCommentsCountDTO, CommentReactionsCountDTO, CommentRepliesCountDTO,
    CommentDTO
)
from gyaan.dtos.dtos import DomainDetailsDTO


@pytest.fixture()
def domain_stats_dto():
    domain_stats = DomainStatsDTO(
        domain_id=1,
        followers_count=5,
        posts_count=10,
        bookmarked_count=15
    )
    return domain_stats


@pytest.fixture()
def domain_dto():
    dto = DomainDTO(
        domain_id=1,
        name="AI/ML",
        description="Artificial Intelligent"
    )
    return dto


@pytest.fixture()
def users_dtos():
    user_dto = [
        UserDetailsDTO(
            user_id=1,
            name="user_1",
            profile_pic_url="profile_pic_url"
        ),
        UserDetailsDTO(
            user_id=2,
            name="user_2",
            profile_pic_url="profile_pic_url"
        )
    ]
    return user_dto

@pytest.fixture()
def requested_users_dto():
    users_dtos = [
        UserDetailsDTO(
            user_id=3,
            name="user_3",
            profile_pic_url="profile_pic_url"
        ),
        UserDetailsDTO(
            user_id=4,
            name="user_4",
            profile_pic_url="profile_pic_url"
        )
    ]
    return users_dtos


@pytest.fixture()
def domain_join_requests_dto():
    domain_join_requests_dtos = [
        DomainJoinRequestDTO(
            request_id=1,
            user_id=3,
        ),
        DomainJoinRequestDTO(
            request_id=2,
            user_id=4,
        )
    ]
    return domain_join_requests_dtos

@pytest.fixture()
def post_dtos():
    post_dto = [
        PostDTO(
            post_id=1,
            posted_at=datetime.datetime.now(),
            posted_by_id=1,
            title="post title",
            content="post content"
        )
    ]
    return post_dto


def tag_dto():
    tag = [TagDTO(
        tag_id=1,
        name="tag name"
    )]
    return tag

def post_tag_dto():
    post_tag = [
        PostTagDTO(
            post_id=1,
            tag_id=1
        )
    ]
    return post_tag

@pytest.fixture()
def post_tag_details_dto():
    post_tag_details = PostTagDetailsDTO(
        tags=tag_dto(),
        post_tag_ids=post_tag_dto()
    )
    return post_tag_details


@pytest.fixture()
def post_reaction_count_dto():
    post_reaction_count = [
        PostReactionsCountDTO(
            post_id=1,
            reactions_count=5
        )
    ]
    return post_reaction_count

@pytest.fixture()
def post_comments_count_dto():
    post_comments_count = [
        PostCommentsCountDTO(
            post_id=1,
            comments_count=5
        )
    ]
    return post_comments_count


@pytest.fixture()
def comment_reaction_count_dto():
    comment_reaction_count = [
        CommentReactionsCountDTO(
            comment_id=1,
            reactions_count=5
        )
    ]
    return comment_reaction_count

@pytest.fixture
def comment_replies_count_dto():
    comment_replies_count = [
        CommentRepliesCountDTO(
            comment_id=1,
            replies_count=5
        )
    ]
    return comment_replies_count

@pytest.fixture()
def comment_dto():
    comment = [
        CommentDTO(
            comment_id=1,
            commented_at=datetime.datetime.now(),
            commented_by_id=1,
            content="comment content"
        )
    ]
    return comment


# @pytest.fixture()
# def domain_details_dto():
#     domain_details = DomainDetailsDTO(
#         domain=
#     )

# @dataclass
# class DomainDetailsDTO:
#     domain: DomainDTO
#     domain_stats: DomainStatsDTO
#     domain_experts: List[UserDetailsDTO]
#     join_requests: List[DomainJoinRequestDTO]
#     requested_users: List[UserDetailsDTO]
#     user_id: int
#     is_user_domain_expert: bool
# 
#         UserDetailsDTO(
#             user_id=5,
#             name="user_5",
#             profile_pic_url="profile_pic_url"
#         )

# @pytest.fixture()
# def 
# get_domain_details_response(DomainDetailsDTO(domain=DomainDTO(domain_id=1,
# name='AI/ML', description='Artificial Intelligent'), domain_stats=DomainStatsDTO(domain_id=1, 
# followers_count=5, posts_count=10, bookmarked_count=15), domain_experts=[UserDetailsDTO(user_id=1,
# name='user_1', profile_pic_url='profile_pic_url'), UserDetailsDTO(user_id=2, name='user_2', 
# profile_pic_url='profile_pic_url')], join_requests=[DomainJoinRequestDTO(request_id=1, user_id=3), 

# DomainJoinRequestDTO(request_id=2, user_id=4)], requested_users=[UserDetailsDTO(user_id=3,
# name='user_3', profile_pic_url='profile_pic_url'), UserDetailsDTO(user_id=4, name='user_4',
# profile_pic_url='profile_pic_url')], user_id=1, is_user_domain_expert=True))