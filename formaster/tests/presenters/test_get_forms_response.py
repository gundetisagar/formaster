from formaster.presenters.presenter_implementation import \
    PresenterImplementation



def test_get_forms_response(form_title_with_id_two_dtos,
                            expected_form_details):
    # Arrange
    presenter = PresenterImplementation()
    expected_form_details = expected_form_details

    # Act
    json = presenter.get_forms_response(form_title_with_id_two_dtos)

    # Act
    assert expected_form_details == json
