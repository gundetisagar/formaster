from django.db import models
from formaster.models.question import Question



class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return "{}--{}".format(self.choice_text, self.question.id)
