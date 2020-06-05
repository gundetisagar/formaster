# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "form_delete"
REQUEST_METHOD = "delete"
URL_SUFFIX = "form_delete/{form_id}/v1/"

from .test_case_01 import TestCase01FormDeleteAPITestCase

__all__ = [
    "TestCase01FormDeleteAPITestCase"
]
