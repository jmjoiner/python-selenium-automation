from selenium.webdriver.common.by import By
from behave import given, when, then

MOST_WANTED = (By.XPATH, '//a[contains(@href, "ref=zg_bs_tab")]')

@given('Open Amazon Bestsellers Page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('User sees {expected_count} subheader links')
def subheader_links(context, expected_count):
    expected_count = int(expected_count)
    subheader_links_count = len(context.driver.find_elements(*MOST_WANTED))
    assert expected_count == subheader_links_count, f'Expected {expected_count}, did not match {subheader_links_count}'