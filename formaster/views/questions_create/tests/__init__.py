# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "questions_create"
REQUEST_METHOD = "post"
URL_SUFFIX = "questions_create/{form_id}/v1/"

from .test_case_01 import TestCase01QuestionsCreateAPITestCase

__all__ = [
    "TestCase01QuestionsCreateAPITestCase"
]
