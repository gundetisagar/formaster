
import factory
from django.utils import timezone
from formaster.models import *


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"username{n}")
    is_admin = True

class FormFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Form

    form_title = factory.Sequence(lambda n: f"title_{n}")
    created_by = factory.SubFactory(UserFactory)
    created_at = factory.LazyFunction(timezone.now)

from formaster.constants.enums import QuestionTypes
list_of_question_types = [
    question_type[0]
    for question_type in Question.question_types
]

class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question_type = factory.Iterator(list_of_question_types)
    question_text = factory.Sequence(lambda n: f"question_{n}")
    required = False
    description = "description"
    image = "image"
    form = factory.Iterator(Form.objects.all())
    created_at = factory.LazyFunction(timezone.now)


class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Choices
    question = factory.Iterator(Question.objects.filter(question_type="MCQ"))
    choice_text = factory.Sequence(lambda n: f"choice_{n}")

