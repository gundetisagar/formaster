from abc import abstractmethod


class ResponseStorageInterface:

    @abstractmethod
    def submit_response(self, user_id: int, question_id: int,
                        response_text: str, choice_id: int):
        pass
