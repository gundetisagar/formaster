
from formaster.presenters.presenter_implementation import \
    PresenterImplementation



def test_add_form_title_response(form_title_with_id_dto):
    # Arrange
    presenter = PresenterImplementation()
    expected_form_details = {
        "form_title": "Snacks Form",
        "form_id": 1
    }

    # Act
    json = presenter.add_form_title_response(form_title_with_id_dto)

    # Act
    assert expected_form_details == json
