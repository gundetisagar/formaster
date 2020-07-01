from django.db import models


class Form(models.Model):
    user_id = models.IntegerField()
    form_title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

