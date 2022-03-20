from selenium.webdriver.common.by import By
from behave import given, when, then

TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_header_texrt')
MOST_WANTED = (By.XPATH, '//a[contains(@href, "ref=zg_bs_tab")]')

@given('Open Amazon Bestsellers Page')
def open_prime(context):
    context.app.bestsellers_page.open_amazon_bestsellers()


@then('User sees {expected_count} subheader links')
def subheader_links(context, expected_count):
    context.app.bestsellers_page.open_amazon_bestsellers()

