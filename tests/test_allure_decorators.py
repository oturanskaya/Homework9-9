import allure
from selene import browser, by, be


def test_issue_decorator(browser_config):
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    go_to_issues()
    searching_issue('Issue_created_to_test_allure_reports')


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('/')


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step("Открываем репозиторий {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Переходим на вкладку issues")
def go_to_issues():
    browser.element('#issues-tab').click()


@allure.step("Ищем задачу с номером {item}")
def searching_issue(item):
    browser.element(by.partial_text(item)).should(be.visible)