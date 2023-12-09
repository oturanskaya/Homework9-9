from selene import browser, by, be


def test_issue_pure(browser_config):
    browser.open('/')

    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()
    browser.element(by.partial_text('Issue_created_to_test_allure_reports')).should(be.visible)
