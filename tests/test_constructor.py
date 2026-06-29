import pytest

from locators import ConstructorPageLocators
from url import MAIN_URL
from helpers import open_page, is_tab_active, click_tab


TABS = [
    (ConstructorPageLocators.TAB_BUNS, "Булки"),
    (ConstructorPageLocators.TAB_SAUCES, "Соусы"),
    (ConstructorPageLocators.TAB_FILLINGS, "Начинки"),
]


class TestConstructor:

    @pytest.mark.parametrize("tab_locator, tab_name", TABS)
    def test_tab_becomes_active(self, driver, tab_locator, tab_name):
        """Переход на вкладку делает её активной.
        «Булки» активна по умолчанию, поэтому для надёжности сначала
        переключаемся на «Соусы», чтобы доказать, что клик меняет
        активную вкладку, а не просто видит уже активное состояние."""
        open_page(driver, MAIN_URL)
        click_tab(driver, ConstructorPageLocators.TAB_SAUCES)

        tab_container = click_tab(driver, tab_locator)

        assert is_tab_active(tab_container), f"Вкладка «{tab_name}» не стала активной"
