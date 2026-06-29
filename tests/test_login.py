from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators, RegisterPageLocators, ForgotPasswordPageLocators
from url import MAIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL
from helpers import open_page, login_with_existing_user


class TestLogin:

    def test_login_via_main_button(self, driver):
        #Вход по кнопке «Войти в аккаунт» на главной.
        open_page(driver, MAIN_URL)
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)
        )
        login_button.click()

        order_button = login_with_existing_user(driver)
        assert order_button.is_displayed()

    def test_login_via_account_link(self, driver):
        #Вход по кнопке «Личный кабинет» в хедере.
        open_page(driver, MAIN_URL)
        account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        )
        account_link.click()

        order_button = login_with_existing_user(driver)
        assert order_button.is_displayed()

    def test_login_from_register_page(self, driver):
        #Вход по кнопке «Войти» на странице регистрации.
        open_page(driver, REGISTER_URL)
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)
        )
        login_link.click()

        order_button = login_with_existing_user(driver)
        assert order_button.is_displayed()

    def test_login_from_forgot_password_page(self, driver):
        #Вход по кнопке «Войти» на странице восстановления пароля.
        open_page(driver, FORGOT_PASSWORD_URL)
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)
        )
        login_link.click()

        order_button = login_with_existing_user(driver)
        assert order_button.is_displayed()
