# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "user_get_forms"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/get_forms/v1/"

from .test_case_01 import TestCase01UserGetFormsAPITestCase

__all__ = [
    "TestCase01UserGetFormsAPITestCase"
]
