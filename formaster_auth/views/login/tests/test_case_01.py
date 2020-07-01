"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "username": "username",
    "password": "password"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}
from formaster_auth.models.user import User
import factory

def create_user_01():
    User.objects.create_user(
        username="username",
        password="password",
        is_admin=True
    )


# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     username = "username"
#     password = "password"
#     is_admin = True

class TestCase01LoginAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    #UserFactory.reset_sequence()
    create_user_01()
    print("*"*100)
    print(User.objects.all().values())
    print("*"*100)

    def test_case(self):
        response = self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
        import json
        access_details = json.loads(response.content)
