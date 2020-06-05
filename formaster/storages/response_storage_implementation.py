from formaster.interactors.storages.response_storage_interface import \
    ResponseStorageInterface
from formaster.models.response import Response


class ResponseStorageImplementation(ResponseStorageInterface):

    def submit_response(self, user_id: int, question_id: int,
                        response_text: str, choice_id: int):
        Response.objects.create(
            response_by_id=user_id,
            question_id=question_id,
            response_text=response_text,
            choice_id=choice_id
        )
