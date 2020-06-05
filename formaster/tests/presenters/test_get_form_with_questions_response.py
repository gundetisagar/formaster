from formaster.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_form_with_questions_response(form_with_questions_dto,
                                          list_of_questions_dict):
    # Arrange
    presenter = PresenterImplementation()
    form_with_questions_dto = form_with_questions_dto
    expected_form_with_questions_dict = list_of_questions_dict

    # Act
    json = presenter.get_form_with_questions_response(
        form_with_questions_dto
    )

    # Act
    assert expected_form_with_questions_dict == json
