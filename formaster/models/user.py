from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, models.Model):
    is_admin = models.BooleanField(default=False)


    # def __str__(self):
    #     return "{}".format(self.username)

import factory

class UserFactory(factory.Factory):
    class Meta:
        model = User
    # username = factory.Sequence(lambda n: "user%d" % n)
    # or
    #  @factory.sequence

    @factory.sequence
    def username(n):
        return "username_{}".format(n)

"""

from formaster.models.user import UserFactory
from formaster.models.form import Form


"""