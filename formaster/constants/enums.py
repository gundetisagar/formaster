import enum


class QuestionTypes(enum.Enum):
    WELCOME_SCREEN = "WELCOME_SCREEN"
    LARGE_TEXT = "LARGE_TEXT"
    SMALL_TEXT = "SMALL_TEXT"
    MCQ = "MCQ"
    THANK_YOU_SCREEN = "THANK_YOU_SCREEN"


TYPES_OF_TEXT_QUESTIONS = [QuestionTypes.WELCOME_SCREEN.value,
                           QuestionTypes.THANK_YOU_SCREEN.value,
                           QuestionTypes.SMALL_TEXT.value,
                           QuestionTypes.LARGE_TEXT.value]
