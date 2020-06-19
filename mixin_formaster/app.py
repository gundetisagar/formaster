from django.apps import AppConfig


class MixinFormasterAppConfig(AppConfig):
    name = "mixin_formaster"

    def ready(self):
        from mixin_formaster import signals # pylint: disable=unused-variable
