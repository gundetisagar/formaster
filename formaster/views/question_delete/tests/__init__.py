# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "question_delete"
REQUEST_METHOD = "delete"
URL_SUFFIX = "question_delete/{form_id}/{question_id}/v1/"

from .test_case_01 import TestCase01QuestionDeleteAPITestCase

__all__ = [
    "TestCase01QuestionDeleteAPITestCase"
]
