import factory
from efficient_fixture_management.models.user import User


class UserFactory(factory.Factory):
    class Meta:
        models = User

    first_name = "user_first_name"
    last_name = "user_last_name"



"""

from efficient_fixture_management.models.user import User
from efficient_fixture_management.utils.factories import UserFactory

"""