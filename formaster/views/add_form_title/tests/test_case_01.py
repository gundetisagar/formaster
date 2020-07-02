"""
Create New Form
"""

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from formaster.utils.custom_test_utils import CustomTestUtils


REQUEST_BODY = """
{
    "form_title": "my first form"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01AddFormTitleAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01AddFormTitleAPITestCase, self).setupUser(
            username=username, password=password
        )

        user = self.foo_user
        user.is_admin=True
        user.save()


    def test_case(self):
        response = self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.

        import json

        form_title = json.loads(response.content)

        from formaster.models import Form
        form_obj = Form.objects.get(id=1)
        self.assert_match_snapshot(
            name="form_id",
            value=form_obj.id
        )
        self.assert_match_snapshot(
            name="form title",
            value=form_obj.form_title
        )
