import pytest
from formaster.dtos.dtos import (
    UserDetailsDto,
)


@pytest.fixture()
def user_profile_dto():
    user_details_dto = UserDetailsDto(
        user_id=1,
        username="user",
        is_admin=True
    )
    return user_details_dto
