from module14.common.hw14 import DemoblizeHomePage
from selenium import webdriver

import pytest

@pytest.fixture(scope='function')
def driver():
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    yield _driver
    _driver.quit()


@pytest.fixture
def login(driver):
    test_page = DemoblizeHomePage(driver)
    test_page.open_home_page()
    test_page.open_log_in_form()
    test_page.log_in()