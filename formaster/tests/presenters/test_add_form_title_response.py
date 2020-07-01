
from formaster.presenters.presenter_implementation import \
    PresenterImplementation



def test_add_form_title_response(form_details_dto):
    # Arrange
    presenter = PresenterImplementation()
    expected_form_details = {
        "form_title": "Snacks Form",
        "form_id": 1
    }

    # Act
    form_details_dict = presenter.add_form_title_response(form_details_dto)

    # Act
    assert expected_form_details == form_details_dict
