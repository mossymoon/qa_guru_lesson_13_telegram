import allure
from selene import have, by


@allure.title("Registration form success")
def test_successful(setup_browser):
    browser = setup_browser

    with allure.step("Открыть регистрационную форму"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Заполнить регистрационную форму"):
        browser.element("#firstName").set_value("Ivan")
        browser.element("#lastName").set_value("Ivanov")
        browser.element("#userEmail").set_value("asas@mail.ru")
        browser.element("#genterWrapper").element(by.text("Other")).click()
        browser.element("#userNumber").set_value("1231231230")
        # browser.element("#dateOfBirthInput").click()
        # browser.element(".react-datepicker__month-select").s("July")
        # browser.element(".react-datepicker__year-select").selectOption("2008")
        # browser.element(".react-datepicker__day--030:not(.react-datepicker__day--outside-month)").click()
        browser.element("#subjectsInput").send_keys("Maths")
        browser.element("#subjectsInput").press_enter()
        browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
        # browser.element("#uploadPicture").uploadFromClasspath("img/1.png")
        browser.element("#currentAddress").set_value("Some street 1")
        browser.element("#state").click()
        browser.element("#stateCity-wrapper").element(by.text("NCR")).click()
        browser.element("#city").click()
        browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()
        browser.element("#submit").click()

    with allure.step("Проверить результат"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
        
