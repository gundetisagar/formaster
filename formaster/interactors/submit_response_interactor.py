from typing import List
from formaster.interactors.storages.response_storage_interface import \
    ResponseStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.storages.question_storage_interface import \
    QuestionStorageInterface
from formaster.interactors.storages.choice_storage_interface import \
    ChoiceStorageInterface
from formaster.dtos.dtos import SubmitResponseDto
from formaster.exceptions.exceptions import InvalidQuestionId, InvalidChoiceId



class SubmitResponseInteractor:
    def __init__(self, response_storage: ResponseStorageInterface,
                 questions_storage: QuestionStorageInterface,
                 choice_storage: ChoiceStorageInterface,
                 presenter: PresenterInterface):
        self.response_storage = response_storage
        self.questions_storage = questions_storage
        self.choice_storage = choice_storage
        self.presenter = presenter

    def submit_response(self, user_id: int, response_list: list):
        user_id = user_id
        response_list = response_list

        for response in response_list:
            question_id = response['question_id']
            try:
                self.questions_storage.validate_question_id(
                    question_id=question_id
                )
            except InvalidQuestionId:
                self.presenter.raise_exception_for_invalid_question_id()
                return

            choice_id = response['choice_id']
            if choice_id:
                try:
                    self.choice_storage.validate_choice_id(
                        choice_id=choice_id
                    )
                except InvalidChoiceId:
                    self.presenter.raise_exception_for_invalid_choice_id()
                    return

            response_text = response['response_text']
            if response_text or choice_id:
                self.response_storage.submit_response(
                    user_id,
                    question_id,
                    response_text,
                    choice_id
                )
            

        # try:
        #     old_reaction = self.reaction_storage.get_reaction_of_post(
        #         user_id=user_id,
        #         post_id=post_id,
        #     )
        # except ReactionDoesNotExist:
        #     self.reaction_storage.react_to_post(
        #         user_id=user_id,
        #         post_id=post_id,
        #         reaction_type=reaction_type
        #     )
        #     return
        # same_reactions = old_reaction == reaction_type
        # if same_reactions:
        #     self.reaction_storage.delete_reaction_of_post(
        #         user_id=user_id,
        #         post_id=post_id
        #     )
        # else:
        #     self.reaction_storage.update_reaction_of_post(
                # user_id=user_id,
                # post_id=post_id,
                # reaction_type=reaction_type