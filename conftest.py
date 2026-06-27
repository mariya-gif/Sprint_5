import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.set_page_load_timeout(30)

    yield chrome_driver

    chrome_driver.quit()
