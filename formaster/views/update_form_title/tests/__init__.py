# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "update_form_title"
REQUEST_METHOD = "put"
URL_SUFFIX = "update_form_title/{form_id}/v1/"

from .test_case_01 import TestCase01UpdateFormTitleAPITestCase

__all__ = [
    "TestCase01UpdateFormTitleAPITestCase"
]
