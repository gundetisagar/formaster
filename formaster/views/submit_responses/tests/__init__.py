# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "submit_responses"
REQUEST_METHOD = "post"
URL_SUFFIX = "submit_responses/v1/"

from .test_case_01 import TestCase01SubmitResponsesAPITestCase

__all__ = [
    "TestCase01SubmitResponsesAPITestCase"
]
