from django_swagger_utils.utils.test import CustomAPITestCase

from formaster.utils.factories import *

class CustomTestUtils(CustomAPITestCase):

    def create_user_factory(self):
        UserFactory()

    def create_form_factory(self, user):
        FormFactory(created_by=user)

    def get_forms_factory(self, user):
        FormFactory.create_batch(5, created_by=user)


    def get_form_with_questions_factory(self, user):
        FormFactory(created_by=user)
        QuestionFactory.create_batch(3)
        ChoiceFactory()