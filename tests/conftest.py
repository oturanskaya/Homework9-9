import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.window_height = 1200
    browser.config.window_width = 1400
    browser.config.base_url = 'https://github.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    yield

    browser.quit()