from selenium.webdriver.common.by import By
from behave import given, when, then

DELIVERY_BEBEFITS = (By.ID, "prime-benefit-module-content-delivery-item")

@given('Open Amazon Prime page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('User sees {expected_count} delivery benefits')
def verify_benefits_count(context, expected_count):
    expected_count = int(expected_count)
    delivery_benefits_count = len(context.driver.find_element(*DELIVERY_BEBEFITS))
    assert expected_count == delivery_benefits_count, \
        f'Expected {expected_count}, did not match {delivery_benefits_count}'