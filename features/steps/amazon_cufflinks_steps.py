from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from features.steps.product_search import SEARCH_SUBMIT

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
CART_COUNT = (By.CSS_SELECTOR, "#a-autoid-1-announce span.a-dropdown-prompt")

@when('Search for cufflinks')
def search_amazon_cufflinks(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('cufflinks')


@then('Search result have {expected_result}')
def results_have_cufflinks(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "span.a-color-state.a-text-bold").text
    assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_result}'


@when('Click on the first product')
def first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Click on Add to cart button')
def add_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@when('Open Cart Page')
def open_cart_page(context):
    context.driver.find_element(By.ID, "nav-cart-count").click()


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    cart_count_amount = context.driver.find_element(*CART_COUNT).text
    assert cart_count_amount == expected_count, f'Expected {expected_count}, but got {cart_count_amount}'