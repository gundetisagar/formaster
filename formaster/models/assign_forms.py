from django.db import models
from formaster.models import User
from formaster.models import Form


class AssignForm(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}--{}".format(self.form, self.user)
