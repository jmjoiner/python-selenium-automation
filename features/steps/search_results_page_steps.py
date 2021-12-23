from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Search results have {expected_result}')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_result}'
