class DomainDoesNotExist(Exception):
    pass


class UserNotDomainMember(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


class InvalidPostIds(Exception):
    def __init__(self, invalid_post_ids):
        self.invalid_post_ids = invalid_post_ids
