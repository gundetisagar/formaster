from formaster.interactors.storages.response_storage_interface import \
    ResponseStorageInterface
from formaster.models.response import Response


class ResponseStorageImplementation(ResponseStorageInterface):

    def submit_response(self, user_id: int, question_id: int,
                        response_text: str, choice_id: int):

        try:
            old_response = Response.objects.get(response_by_id=user_id,
                                                question_id=question_id)
        except Response.DoesNotExist:
            Response.objects.create(
                response_by_id=user_id,
                question_id=question_id,
                response_text=response_text,
                choice_id=choice_id
            )
            return
        #same_response = old_response.

# try:
#             old_reaction = self.reaction_storage.get_reaction_of_post(
#                 user_id=user_id,
#                 post_id=post_id,
#             )
#         except ReactionDoesNotExist:
#             self.reaction_storage.react_to_post(
#                 user_id=user_id,
#                 post_id=post_id,
#                 reaction_type=reaction_type
#             )
#             return
#         same_reactions = old_reaction == reaction_type
#         if same_reactions:
#             self.reaction_storage.delete_reaction_of_post(
#                 user_id=user_id,
#                 post_id=post_id
#             )
#         else:
#             self.reaction_storage.update_reaction_of_post(
#                 user_id=user_id,
#                 post_id=post_id,
#                 reaction_type=reaction_type
                
#  Reaction.objects.filter(
            # reacted_by_id=user_id,
            # post_id=post_id).update(reaction=reaction_type)