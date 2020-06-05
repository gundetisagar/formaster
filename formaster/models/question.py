from django.db import models
from formaster.models.form import Form
from formaster.constants.enums import QuestionTypes



class Question(models.Model):
    question_type = models.CharField(
        max_length=50,
        choices=[(question_type.value, question_type.name)
                 for question_type in QuestionTypes
                ]
    )
    question_text = models.TextField()
    required = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}--{}--{}".format(self.question_text,
                                 self.question_type, self.form)
