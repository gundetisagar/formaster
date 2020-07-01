from django.db import models
from formaster.models.question import Question
from formaster.models.choices import Choices


class Response(models.Model):
    user_id = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_text = models.TextField(null=True, blank=True)
    choice = models.ForeignKey(
        Choices,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    submited_at = models.DateTimeField(auto_now=True)
