import allure
from selene import browser, by, be


def test_issue_dynamic(browser_config):
    with allure.step("Открываем страницу"):
        browser.open('/')

    with allure.step("Ищем репозиторий"):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    with allure.step("Переходим в репозиторий"):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Переходим на вкладку issues"):
        browser.element('#issues-tab').click()

    with allure.step("Ищем задачу с названием Issue_created_to_test_allure_reports"):
        browser.element(by.partial_text('Issue_created_to_test_allure_reports')).should(be.visible)