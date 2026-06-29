from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators, AccountPageLocators
from url import MAIN_URL, ACCOUNT_URL, LOGIN_URL
from helpers import login_via_main_page


class TestNavigation:

    def test_go_to_account_page(self, driver):
        #Переход в личный кабинет по клику на «Личный кабинет».
        login_via_main_page(driver, MAIN_URL)

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(ACCOUNT_URL))
        assert driver.current_url == ACCOUNT_URL, "Переход в личный кабинет не произошёл"

    def test_go_to_constructor_via_link(self, driver):
        #Переход из личного кабинета в конструктор по ссылке «Конструктор».
        login_via_main_page(driver, MAIN_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(ACCOUNT_URL))

        driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL + "/"))
        assert driver.current_url == MAIN_URL + "/", "Переход в конструктор по ссылке «Конструктор» не произошёл"

    def test_go_to_constructor_via_logo(self, driver):
        #Переход из личного кабинета в конструктор по клику на логотип.
        login_via_main_page(driver, MAIN_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(ACCOUNT_URL))

        driver.find_element(*MainPageLocators.LOGO_LINK).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL + "/"))
        assert driver.current_url == MAIN_URL + "/", "Переход в конструктор по логотипу не произошёл"

    def test_logout(self, driver):
        #Выход из аккаунта по кнопке «Выход» в личном кабинете.
        login_via_main_page(driver, MAIN_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(ACCOUNT_URL))

        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL, "После выхода не произошёл переход на страницу входа"
