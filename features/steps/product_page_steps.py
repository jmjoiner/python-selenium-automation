from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection.hover')


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')



@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ('Black', 'Pewter', 'Powder Blue', 'Rose', 'Spring Green')

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i in range(len(colors)):
        colors[i].click()
        actual_color = context.driver.find_elements(SELECTED_COLOR).text

        assert actual_color == expected_colors[i], f'Expected {expected_colors[i]}, but got {actual_color}'