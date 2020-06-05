# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from formaster.models import (
    User,
    Form,
    Question,
    Choices,
    Response,
    AssignForm
)


admin.site.register(User)
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Choices)
admin.site.register(Response)
admin.site.register(AssignForm)
