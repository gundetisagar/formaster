# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "update_form_questions"
REQUEST_METHOD = "put"
URL_SUFFIX = "update_form_questions/{form_id}/v1/"

from .test_case_01 import TestCase01UpdateFormQuestionsAPITestCase

__all__ = [
    "TestCase01UpdateFormQuestionsAPITestCase"
]
