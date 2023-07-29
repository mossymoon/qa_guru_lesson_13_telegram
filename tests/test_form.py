import os

from selene import browser, be, have
from selene.core import command
from selene.support.shared.jquery_style import s


def test_dificult_form():
    browser.open('automation-practice-form')

    # заполнение формы
    s('#adplus-anchor').perform(command.js.remove)
    s('#fixedban').perform(command.js.remove)

    browser.element('[id=firstName]').should(be.blank).type('Ivan')
    browser.element('[id=lastName]').should(be.blank).type('Ivanov')
    browser.element('[id=userEmail]').should(be.blank).type('ivan@co.com')
    browser.element('.custom-control-label').click()
    browser.element('[id=userNumber]').should(be.blank).type('9999999999')

    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1989"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="11"]').click()
    browser.element('.react-datepicker__day--028').click()
    browser.element('[id="subjectsInput"]').click().send_keys("Maths").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    # browser.element('#uploadPicture').send_keys(os.path.abspath('tests/images/picture.jpeg'))
    browser.element('[id=currentAddress]').type('Москва, ул. Тверская, дом 1')
    browser.element('input#react-select-3-input').type("Haryana").press_enter()
    browser.element('input#react-select-4-input').type("Panipat").press_enter()
    browser.element('[id="submit"]').click()
    browser.element('[id="closeLargeModal"]').click()


    # Проверка формы
    browser.element('.modal-header').should(have.exact_text('Thanks for submitting the form'))

    # Закрытие модального окна
    browser.element('#closeLargeModal').click()
    browser.element('.modal-dialog').should(be.absent)
