import pytest
from formaster_auth.dtos.dtos import (
    UserAuthTokensDto,
    UserDetailsDto
)
from formaster_auth.models.user import User


@pytest.fixture()
def user_auth_token_dto():
    userauthdto = UserAuthTokensDto(
        user_id=1,
        access_token="12345",
        refresh_token="54321",
        expires_in=121313
    )
    return userauthdto


@pytest.fixture()
def user_profile_dtos():
    user_details_dto = UserDetailsDto(
        user_id=1,
        username="user",
        is_admin=True
    )
    return user_details_dto

@pytest.fixture()
def create_user():
    User.objects.create_user(
        username="username",
        password="password",
        is_admin=False
    )

@pytest.fixture()
def create_admin():
    User.objects.create_user(
        username="username",
        password="password",
        is_admin=True
    )
