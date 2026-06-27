from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, ForgotPasswordPageLocators
from url import MAIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL
from data import Credentials


def open_page(driver, url, attempts=2):
    #Открывает страницу с одной повторной попыткой на случай,
    #если сайт ответит с задержкой и страница не успеет загрузиться.
    for attempt in range(attempts):
        try:
            driver.get(url)
            return
        except TimeoutException:
            if attempt == attempts - 1:
                raise


def login_with_existing_user(driver):
    #Вводит email/пароль существующего пользователя и нажимает «Войти»,
    #затем ждёт появления кнопки «Оформить заказ» — признак успешного входа.
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    order_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    )
    return order_button


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
