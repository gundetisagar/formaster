# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "update_form"
REQUEST_METHOD = "post"
URL_SUFFIX = "form_update/{form_id}v1/"

from .test_case_01 import TestCase01UpdateFormAPITestCase

__all__ = [
    "TestCase01UpdateFormAPITestCase"
]
