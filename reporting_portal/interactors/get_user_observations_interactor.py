from reporting_portal.interactors.storages.observation_storage_interface \
    import ObservationStorageInterface
from reporting_portal.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetUserObservationsInteractor:

    def __init__(self, observation_storage: ObservationStorageInterface,
                 presenter: PresenterInterface):
        self.observation_storage = observation_storage
        self.presenter = PresenterInterface

    def get_user_observations_wrapper(self, offset: int, limit: int):
        try:
            