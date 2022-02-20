from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

BOOT_COLOR_CHOICE = (By.CSS_SELECTOR, 'div#variation_color_name ul li')
SELECTED_COLOR = (By.CSS_SELECTOR, 'span.selection')


#@given('Open Amazon product {product_id} page')
#def open_amazon_product(context, product_id):
#   context.driver.get('https://www.amazon.com/VOSTEY-Motorcycle-Bsiness-Casual-BMY680B/dp/B088BJY7DR')



@then('Verify user will click through colors')
def verify_will_click_colors(context):
    expected_colors = ('Motorcycle678a-black', 'Motorcycle678a-dark Brown', 'Bmy684-black')
    context.driver.wait.until(EC.presence_of_all_elements_located(BOOT_COLOR_CHOICE))
    colors = context.driver.find_elements(*BOOT_COLOR_CHOICE)
    for i in range(len(colors))[:3]:
        colors[i].click()
        sleep(3)
        actual_color = context.driver.find_element(*SELECTED_COLOR).text
        #print(len(actual_color))
        assert actual_color == expected_colors[i], f'Expected {expected_colors[i]}, but got {actual_color}'
