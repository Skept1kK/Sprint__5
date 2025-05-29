import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from urls import TestUrls


@pytest.fixture
def get_driver():
        options = Options()
        options.add_argument("--window-size=1300,1200")
        driver = webdriver.Chrome(options=options)
        driver.get(TestUrls.MAIN_PAGE_URL)
        yield driver
        driver.quit()

