from formaster.presenters.presenter_implementation import \
    PresenterImplementation
from formaster.constants.enums import QuestionTypes


# def test_get_form_view_response_with_text_type_question(
#         view_form_response_text_question_dto):
#     # Arrange
#     presenter = PresenterImplementation()
#     expected_view_form_response_dict = {
#         "form_title": "Snacks Form",
#         "form_id": 1,
#         'question_and_response_list': [{
#             'choices': [],
#             'description': 'about create question',
#             'question_id': 1,
#             'question_text': 'create question',
#             'question_type': QuestionTypes.LARGE_TEXT.value,
#             'required': True,
#             'response_choice_id': None,
#             'response_id': 1,
#             'response_text': 'my answer'}
#         ]
#     }


#     # Act
#     return_dict = presenter.get_form_view_response(
#         view_form_response_text_question_dto
#     )

#     # Act
#     assert expected_view_form_response_dict == return_dict


# def test_get_form_view_response_with_mcq_type_question(
#         view_form_response_mcq_question_dto):
#     # Arrange
#     presenter = PresenterImplementation()
#     question_response_dict = {
#         'description': None,
#         'question_id': 1,
#         'question_text': 'quantity of packets',
#         'question_type': QuestionTypes.MCQ.value,
#         'required': True,
#         'response_choice_id': 1,
#         'response_id': 1,
#         'response_text': None,
#         "choices": [
#             {
#                 "choice_id": 1,
#                 "choice_text": "option A"
#             },
#             {
#                 "choice_id": 2,
#                 "choice_text": "option B"
#             }
#         ]
#     }
#     expected_view_form_response_dict = {
#         "form_title": "Snacks Form",
#         "form_id": 1,
#         'question_and_response_list': [
#             question_response_dict
#         ]
#     }


#     # Act
#     return_dict = presenter.get_form_view_response(
#         view_form_response_mcq_question_dto
#     )

#     # Act
#     assert expected_view_form_response_dict == return_dict
