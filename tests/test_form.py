import allure

from pages.demoqa_form import RegistrationPage
from pages.registration_page import UserPageFillForm

def test_user_registration():
    new_user = UserPageFillForm()
    registration = RegistrationPage()
    with allure.step("Open registrations form"):
        registration.open()
    with allure.step("Fill form"):
        registration.fill_registration_form(user=new_user)
        registration.submit_form()
    with allure.step("Check form results"):
        registration.validate_form(user=new_user)
        registration.close_validation_window()
