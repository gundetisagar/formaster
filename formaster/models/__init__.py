from formaster.models.user import User
from formaster.models.choices import Choices
from formaster.models.form import Form
from formaster.models.question import Question
from formaster.models.response import Response
from formaster.models.assign_forms import AssignForm


__all__ = [
    "User",
    "Choices",
    "Form",
    "Question",
    "Response",
    "AssignForm"
]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
