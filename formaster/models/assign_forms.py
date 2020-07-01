from django.db import models
from formaster.models import Form


class AssignForm(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    user_id = models.IntegerField()
