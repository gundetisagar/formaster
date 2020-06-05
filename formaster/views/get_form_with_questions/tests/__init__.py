# pylint: disable=wrong-import-position

APP_NAME = "formaster"
OPERATION_NAME = "get_form_with_questions"
REQUEST_METHOD = "get"
URL_SUFFIX = "get_form_with_questions/{form_id}/v1/"

from .test_case_01 import TestCase01GetFormWithQuestionsAPITestCase

__all__ = [
    "TestCase01GetFormWithQuestionsAPITestCase"
]
