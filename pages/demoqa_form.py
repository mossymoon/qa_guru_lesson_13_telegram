from selene import browser, be, have
from selene.core import command
from pages.registration_page import UserPageFillForm
from tests import paths


class RegistrationPage:
    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td').even

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def fill_registration_form(self, user: UserPageFillForm):
        browser.element('[id=firstName]').should(be.blank).type(user.first_name)
        browser.element('[id=lastName]').should(be.blank).type(user.last_name)
        browser.element('[id=userEmail]').should(be.blank).type(user.email)
        browser.element('.custom-control-label').click()
        browser.element('[id=userNumber]').should(be.blank).type(user.phone)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(user.year_birthday).click()
        browser.element('.react-datepicker__month-select').send_keys(user.month_birthday).click()
        browser.element(f'.react-datepicker__day--0{user.day_birthday}:not(.react-datepicker__day--outside-month)').click()
        browser.element('[id="subjectsInput"]').click().send_keys(user.subject).press_enter()
        browser.element('[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view)
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#uploadPicture').set_value(paths.get_path_to_photo(user.picture))
        browser.element('[id=currentAddress]').type(user.address)
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.state)
        ).click()
        browser.element('#city').perform(command.js.scroll_into_view)
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.city)
        ).click()

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

    def validate_form(self, user: UserPageFillForm):
        full_name = f'{user.first_name} {user.last_name}'
        inform = 'Thanks for submitting the form'
        browser.element('.modal-header').should(have.exact_text(inform))
        browser.all('.modal-body tr td')[1].should(have.exact_text(full_name))
        browser.all('.modal-body tr td')[3].should(have.exact_text(user.email))
        browser.all('.modal-body tr td')[5].should(have.exact_text(user.gender))
        browser.all('.modal-body tr td')[7].should(have.exact_text(user.phone))
        browser.all('.modal-body tr td')[9].should(have.exact_text(f'{user.day_birthday} '
                                                                   f'{user.month_birthday},'
                                                                   f'{user.year_birthday}'))
        browser.all('.modal-body tr td')[11].should(have.exact_text(user.subject))
        browser.all('.modal-body tr td')[13].should(have.exact_text(user.hobby))
        browser.all('.modal-body tr td')[15].should(have.exact_text(user.picture))
        browser.all('.modal-body tr td')[17].should(have.exact_text(user.address))
        browser.all('.modal-body tr td')[19].should(have.text(f'{user.state} {user.city}'))

    def close_validation_window(self):
        browser.element('[id="closeLargeModal"]').click()
