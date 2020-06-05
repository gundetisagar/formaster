# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "update_question"
REQUEST_METHOD = "put"
URL_SUFFIX = "question_update/{form_id}/{question_id}/v1/"

from .test_case_01 import TestCase01UpdateQuestionAPITestCase

__all__ = [
    "TestCase01UpdateQuestionAPITestCase"
]
