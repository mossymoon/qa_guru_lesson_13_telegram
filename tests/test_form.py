from pages.demoqa_form import RegistrationPage
from pages.registration_page import UserPageFillForm


def test_user_registration():
    new_user = UserPageFillForm()
    registration = RegistrationPage()
    registration.open()
    registration.fill_registration_form(user=new_user)
    registration.submit_form()
    registration.validate_form(user=new_user)
    registration.close_validation_window()
