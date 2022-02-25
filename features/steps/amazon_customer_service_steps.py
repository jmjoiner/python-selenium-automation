from selenium.webdriver.common.by import By
from behave import given, when, then

ELEMENT_OPTIONS = (By.CSS_SELECTOR, "div.a-box-inner div.a-column.a-span3")

@given('Open Amazon CUstomer Service page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('User will see {expected_count} UI elements')
def user_interface_elements(context, expected_count):
    expected_count = int(expected_count)
    elements_count = len(context.driver.find_elements(*ELEMENT_OPTIONSgi))
    assert expected_count == elements_count, f'Expected {expected_count}, did not match {elements_count}'