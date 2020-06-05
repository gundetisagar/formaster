# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "add_form_title"
REQUEST_METHOD = "post"
URL_SUFFIX = "add_form_title/v1/"

from .test_case_01 import TestCase01AddFormTitleAPITestCase

__all__ = [
    "TestCase01AddFormTitleAPITestCase"
]
