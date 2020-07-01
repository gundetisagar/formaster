# pylint: disable=wrong-import-position

APP_NAME = "formaster_auth"
OPERATION_NAME = "get_profile"
REQUEST_METHOD = "get"
URL_SUFFIX = "get_profile/v1/"

from .test_case_01 import TestCase01GetProfileAPITestCase

__all__ = [
    "TestCase01GetProfileAPITestCase"
]
