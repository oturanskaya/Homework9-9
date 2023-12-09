import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "oturanskaya")
@allure.feature("Задачи в репозитории")
@allure.story("Неавторизованный пользователь может просмотреть список задач")
@allure.link("https://github.com", name="Testing")
def test_issue_labels(browser_config):
    browser.open('/')

    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()
    browser.element(by.partial_text('Issue_created_to_test_allure_reports')).should(be.visible)
