from selenium.webdriver.common.by import By
from behave import given, when, then


REGULAR_NAME = (By.CSS_SELECTOR, '.a-row span.a-size-small.a-color-tertiary.wfm-sales-item-card__regular-price')

@given('Open Amazon Whole Foods Page')
def open_google(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')

@then('Verify Product Names')
def verify_product_names(context):
    elements = context.driver.find_elements(*REGULAR_NAME)
    for element in elements:
        assert 'Regular' in element.text