import enum


class QuestionTypes(enum.Enum):
    WELCOME_SCREEN = "WElCOME_SCREEN"
    THANK_YOU_SCREEN = "THANK_YOU_SCREEN"
    MCQ = "MCQ"
    LARGE_TEXT = "LARGE_TEXT"
    SMALL_TEXT = "SMALL_TEXT"


TYPES_OF_TEXT_QUESTIONS = [QuestionTypes.WELCOME_SCREEN.value,
                           QuestionTypes.THANK_YOU_SCREEN.value,
                           QuestionTypes.SMALL_TEXT.value,
                           QuestionTypes.LARGE_TEXT.value]
