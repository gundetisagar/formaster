from django.db import models
from formaster.models.question import Question
from formaster.models.choices import Choices
from formaster.models.user import User



class Response(models.Model):
    response_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_text = models.TextField(null=True, blank=True)
    choice = models.ForeignKey(
        Choices,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    submited_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}--{}--{}".format(self.question, self.response_text, self.choice)
