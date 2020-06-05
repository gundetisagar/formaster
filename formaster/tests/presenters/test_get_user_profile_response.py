from formaster.presenters.presenter_implementation import \
    PresenterImplementation



def test_get_user_profile_response(user_profile_dto):
    # Arrange
    presenter = PresenterImplementation()
    user_profile_dto = user_profile_dto
    expected_user_profile_dict = {
        "user_id": 1,
        "username": "user",
        "is_admin": True
    }

    # Act
    json = presenter.get_user_profile_response(user_profile_dto)

    # Assert
    assert expected_user_profile_dict == json
