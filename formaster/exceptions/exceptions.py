
class InvalidQuestionType(Exception):
    pass

class InvalidQuestionId(Exception):
    pass

class InvalidChoiceId(Exception):
    pass


class InvalidFormId(Exception):
    pass

class FormDoesNotExist(Exception):
    pass

class UserCannotDeleteFormException(Exception):
    pass

class UserCannotUpdateFormException(Exception):
    pass

class UserIsNotCreaterOfForm(Exception):
    pass

class InvalidResponseForm(Exception):
    pass
