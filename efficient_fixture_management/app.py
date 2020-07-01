from django.apps import AppConfig


class EfficientFixtureManagementAppConfig(AppConfig):
    name = "efficient_fixture_management"

    def ready(self):
        from efficient_fixture_management import signals # pylint: disable=unused-variable
