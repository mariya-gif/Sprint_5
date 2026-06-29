import pytest
from selenium.webdriver.support.wait import WebDriverWait

from locators import RegisterPageLocators
from url import REGISTER_URL, LOGIN_URL
from generators import generate_random_credentials


class TestRegistration:

    def test_successful_registration(self, driver):
        name, email, password = generate_random_credentials()

        driver.get(REGISTER_URL)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url == LOGIN_URL)
        assert driver.current_url == LOGIN_URL, "После регистрации не произошёл переход на страницу входа"

    def test_registration_invalid_password(self, driver):
        name, email, _ = generate_random_credentials()
        invalid_password = "123"

        driver.get(REGISTER_URL)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(invalid_password)
        driver.find_element(*RegisterPageLocators.SUBMIT_BUTTON).click()

        error_message = driver.find_element(*RegisterPageLocators.ERROR_MESSAGE)
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
