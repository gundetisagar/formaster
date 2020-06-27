"""
Delete Form
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {"form_id": 1},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["admin"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}
from formaster.utils.custom_test_utils import CustomTestUtils
from formaster.models import *


class TestCase01FormDeleteAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01FormDeleteAPITestCase, self).setupUser(
            username=username, password=password
        )
        user = self.foo_user
        user.is_admin=True
        user.save()
        user = self.foo_user

        self.create_form_factory(user)

        print("*"*100)
        print(User.objects.all().values())
        print(Form.objects.all().values())
        print("*"*100)

    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.

        is_form_exists = Form.objects.filter(id=1).exists()

        self.assert_match_snapshot(
            name="form doesnot exists",
            value=is_form_exists
        )