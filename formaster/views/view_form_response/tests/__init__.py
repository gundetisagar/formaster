# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "view_form_response"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/view_form_response/{form_id}/v1/"

from .test_case_01 import TestCase01ViewFormResponseAPITestCase

__all__ = [
    "TestCase01ViewFormResponseAPITestCase"
]
