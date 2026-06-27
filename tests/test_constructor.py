from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators import ConstructorPageLocators
from url import MAIN_URL


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


def is_tab_active(tab_element):
    #Проверяет, что у вкладки в классе присутствует tab_tab_type_current —
    #признак того, что вкладка активна.
    return "tab_tab_type_current" in tab_element.get_attribute("class")


def click_tab(driver, tab_locator):
    #Кликает по родительскому div вкладки через JavaScript — обходит
    #перекрытие элементов, которое иногда возникает во время рендера страницы.
    tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(tab_locator)
    )
    tab_container = tab.find_element("xpath", "./..")
    driver.execute_script("arguments[0].click();", tab_container)
    return tab_container


class TestConstructor:

    def test_buns_tab(self, driver):
        #Переход на вкладку «Булки» делает её активной.
        #«Булки» активна по умолчанию, поэтому сначала переключаемся
        #на «Соусы», чтобы доказать, что клик реально меняет активную вкладку.
        open_page(driver, MAIN_URL)
        click_tab(driver, ConstructorPageLocators.TAB_SAUCES)

        tab_container = click_tab(driver, ConstructorPageLocators.TAB_BUNS)

        WebDriverWait(driver, 10).until(lambda d: is_tab_active(tab_container))
        assert is_tab_active(tab_container), "Вкладка «Булки» не стала активной"

    def test_sauces_tab(self, driver):
        #Переход на вкладку «Соусы» делает её активной.
        open_page(driver, MAIN_URL)

        tab_container = click_tab(driver, ConstructorPageLocators.TAB_SAUCES)

        WebDriverWait(driver, 10).until(lambda d: is_tab_active(tab_container))
        assert is_tab_active(tab_container), "Вкладка «Соусы» не стала активной"

    def test_fillings_tab(self, driver):
        #Переход на вкладку «Начинки» делает её активной.
        open_page(driver, MAIN_URL)

        tab_container = click_tab(driver, ConstructorPageLocators.TAB_FILLINGS)

        WebDriverWait(driver, 10).until(lambda d: is_tab_active(tab_container))
        assert is_tab_active(tab_container), "Вкладка «Начинки» не стала активной"
