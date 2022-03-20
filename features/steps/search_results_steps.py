from selenium.webdriver.common.by import By
from behave import given, when, then

RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-color-state a-text-bold']")


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('Search results have {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_results_page.verify_search_result(expected_result)
