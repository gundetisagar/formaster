def my_func():
	return 2


def add_positive_numbers(value_1, value_2):
	return value_1 + value_2

def add_float_numbers(value_1, value_2):
	return value_1 + value_2


def test_add_positive_numbers(snapshot):

	return_value = add_positive_numbers(2,2)

	assert return_value == 4

	snapshot.assert_match(return_value, "add_positive_numbers_respose")


def test_add_float_numbers(snapshot):
	return_value = add_float_numbers(3.0, 1.5)

	assert return_value == 4.5

	snapshot.assert_match(return_value, "add_float_numbers_response")


def test_mything(snapshot):
	return_value = my_func()

	assert return_value == 2
	snapshot.assert_match(return_value, "gpg_response")


def test_something(snapshot):
	snapshot.assert_match([1,2,3,4], "list")