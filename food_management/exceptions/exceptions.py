

class InvalidDate(Exception):
    pass

class InvalidMealId(Exception):
    def __init__(self, invalid_meal_id):
        self.invalid_meal_id = invalid_meal_id
