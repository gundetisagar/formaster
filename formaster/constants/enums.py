import enum


class QuestionTypes(enum.Enum):
    WELCOME_SCREEN = "WELCOME_SCREEN"
    THANK_YOU_SCREEN = "THANK_YOU_SCREEN"
    MCQ = "MCQ"
    LARGE_TEXT = "LARGE_TEXT"
    SMALL_TEXT = "SMALL_TEXT"


LIST_OF_QUESTION_TYPES = [(question_type.value)
                          for question_type in QuestionTypes
]
