from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import LoginPageLocators, MainPageLocators
from data import Credentials


def open_page(driver, url, timeout=35):
    #Открывает страницу и ждёт, пока документ полностью загрузится
    driver.get(url)
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )


def is_tab_active(tab_element):
    #Проверяет, что у вкладки в классе присутствует tab_tab_type_current —
    #признак того, что вкладка активна.
    return "tab_tab_type_current" in tab_element.get_attribute("class")


def click_tab(driver, tab_locator):
    #Кликает по родительскому div вкладки — обходит перекрытие элементов
    tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(tab_locator)
    )
    tab_container = tab.find_element("xpath", "./..")
    driver.execute_script("arguments[0].click();", tab_container)
    return tab_container


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


def login_via_main_page(driver, main_url):
    #Авторизует пользователя: открывает MAIN_URL, кликает «Войти в аккаунт» 
    #и вводитданные существующего пользователя.
    open_page(driver, main_url)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)
    )
    login_button.click()

    login_with_existing_user(driver)
