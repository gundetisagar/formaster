from django.db import models
from formaster.models.user import User


class Form(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    form_title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.form_title)
