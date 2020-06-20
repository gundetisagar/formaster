class InvalidUserId(Exception):
    pass

class InvalidPassword(Exception):
    pass

class InvalidUsername(Exception):
    pass

class DoesNotExist(Exception):
    pass

class InvalidQuestionType(Exception):
    pass


class InvalidQuestionId(Exception):
    pass

class InvalidChoiceId(Exception):
    pass


class InvalidFormId(Exception):
    pass

class UserCannotDeleteFormException(Exception):
    pass

class UserCannotUpdateFormException(Exception):
    pass

class UserIsNotAdmin(Exception):
    pass

class UserIsNotCreaterOfForm(Exception):
    pass

class InvalidResponseForm(Exception):
    pass

class UserNotAdmin(Exception):
    pass
