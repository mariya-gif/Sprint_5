from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators import MainPageLocators, LoginPageLocators, AccountPageLocators
from url import MAIN_URL, ACCOUNT_URL, LOGIN_URL
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


def login(driver):
    #Авторизует пользователя через главную страницу и дожидается
    #появления кнопки «Оформить заказ»
    open_page(driver, MAIN_URL)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)
    )
    login_button.click()

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    )


class TestNavigation:

    def test_go_to_account_page(self, driver):
        #Переход в личный кабинет по клику на «Личный кабинет».
        login(driver)

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(ACCOUNT_URL))
        assert driver.current_url == ACCOUNT_URL, "Переход в личный кабинет не произошёл"

    def test_go_to_constructor_via_link(self, driver):
        #Переход из личного кабинета в конструктор по ссылке «Конструктор».
        login(driver)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(ACCOUNT_URL))

        driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL + "/"))
        assert driver.current_url == MAIN_URL + "/", "Переход в конструктор по ссылке «Конструктор» не произошёл"

    def test_go_to_constructor_via_logo(self, driver):
        #Переход из личного кабинета в конструктор по клику на логотип.
        login(driver)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(ACCOUNT_URL))

        driver.find_element(*MainPageLocators.LOGO_LINK).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL + "/"))
        assert driver.current_url == MAIN_URL + "/", "Переход в конструктор по логотипу не произошёл"

    def test_logout(self, driver):
        #Выход из аккаунта по кнопке «Выход» в личном кабинете.
        login(driver)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(ACCOUNT_URL))

        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL, "После выхода не произошёл переход на страницу входа"
