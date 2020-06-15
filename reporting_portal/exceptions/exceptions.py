class InvalidTitleContent(Exception):
    pass

class InvalidDescriptionContent(Exception):
    pass

class InvalidCategoryId(Exception):
    def __init__(self, invalid_category_id):
        self.invalid_category_id = invalid_category_id

class InvalidSubCategoryId(Exception):
    def __init__(self, invalid_sub_category_id):
        self.invalid_sub_category_id = invalid_sub_category_id

class InvalidTitleLength(Exception):
    pass

class InvalidDescriptionLength(Exception):
    pass
