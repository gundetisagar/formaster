from django.db import models
from formaster.models.user import User


class Form(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    form_title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return "{}".format(self.created_at)


import factory
from datetime import datetime
from datetime import date

class FormFactory(factory.Factory):
    class Meta:
        model = Form

    # created_at = factory.LazyFunction(datetime.now)
    form_title = factory.Sequence(lambda n: "username%d" % n)
    #created_at = datetime.now()
    # created_at = factory.LazyAttribute(lambda obj: "{}@{}".format(obj.form_title, datetime.now()))
    @factory.lazy_attribute
    def created_at(self):
        return "%s@example.com" % self.form_title


class Sagar:
    def __init__(self, first_name, last_name, group, admin):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.admin = admin


    def __repr__(self):
        return "{}{}{}".format(self.first_name, self.last_name, self.group)

class SagarFactory(factory.Factory):
    class Meta:
        model = Sagar
    first_name = "first_name"
    last_name = "last_name"
    group = "users"
    admin = "admins"


    #username = "{}@{}".format(first_name,last_name)

# class Admin(Sagar):
#     def __init__(self, first_name, last_name, group, admin):
#         super().__init__(first_name, last_name, group)
#         self.admin = admin
#         self.group = group


#     def __repr__(self):
#         return "{}-{}".format(self.admin, self.group)

class AdminFactory(SagarFactory):
    admin = True
    group = "admins"

    # username = factory.Sequence(lambda n: "first_name%d" % n)

from factory.fuzzy import FuzzyDate
from datetime import timedelta
class Rental:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __repr__(self):
        return f"{self.begin}----{self.end}"

class RentalFactory(factory.Factory):
    class Meta:
        model = Rental
    begin = FuzzyDate(date(2020, 6, 22))
    end = factory.LazyAttribute(lambda obj: obj.begin + timedelta(obj.duration))

    class Params:
        duration = 12

"""
super().__init__(color,max_speed,acceleration,tyre_friction)
from formaster.models.form import SagarFactory, AdminFactory
from formaster.models.form import RentalFactory
import datetime

"""