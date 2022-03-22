from selenium.webdriver.common.by import By
from behave import given, when, then

RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class='a-row a-size-base a-color-base'] [class*='a-size-base a-link-normal'] [class='a-price'] [aria-hidden='true']")


@when('Click on the first product')
def click_first_product(context):
    # context.driver.find_element(*PRODUCT_PRICE).click()
    context.app.search_results_page.click_first_product()


@then('Search results have {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_results_page.verify_search_result(expected_result)
