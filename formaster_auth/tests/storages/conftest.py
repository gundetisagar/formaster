import pytest
#from datetime import datetime
#from freezegun import freeze_time
from formaster_auth.models.user import User
from formaster_auth.dtos.dtos import UserDetailsDto


@pytest.fixture()
def create_user():
    password="password"
    user = User.objects.create(
        username="username",
        is_admin=True
    )
    user.set_password(password)
    user.save()
    #return user

@pytest.fixture()
def create_second_user():
    user = User.objects.create(
        username="username_2",
        password="password_2",
        is_admin=False
    )
    user.set_password(user.password)
    user.save()
    #return user
