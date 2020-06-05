# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "get_user_forms"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/get_forms/v1/"

from .test_case_01 import TestCase01GetUserFormsAPITestCase

__all__ = [
    "TestCase01GetUserFormsAPITestCase"
]
