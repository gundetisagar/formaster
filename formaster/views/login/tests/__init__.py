# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "login"
REQUEST_METHOD = "post"
URL_SUFFIX = "login/v1/"

from .test_case_01 import TestCase01LoginAPITestCase

__all__ = [
    "TestCase01LoginAPITestCase"
]
