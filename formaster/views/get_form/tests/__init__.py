# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "get_form"
REQUEST_METHOD = "get"
URL_SUFFIX = "get_forms/v1/"

from .test_case_01 import TestCase01GetFormAPITestCase

__all__ = [
    "TestCase01GetFormAPITestCase"
]
