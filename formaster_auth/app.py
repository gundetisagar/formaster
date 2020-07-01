from django.apps import AppConfig


class FormasterAuthAppConfig(AppConfig):
    name = "formaster_auth"

    def ready(self):
        from formaster_auth import signals # pylint: disable=unused-variable
