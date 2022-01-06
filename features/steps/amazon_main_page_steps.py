from selenium.webdriver.common.by import By
from behave import given, when, then

HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "td.navFooterDescItem a")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {keyword}')
def search_amazon(context, keyword):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(keyword)


@when('Click search icon')
def click_search_icon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify hamburger menu is present')
def verify_ham_menu_present(context):
    # element_count = len(context.driver.find_elements(*HAM_MENU))
    # assert element_count == 1, f'Expect to see 1 option, but got {element_count}'
    context.driver.find_element(*HAM_MENU)


@then('Verify {expected_amount} links present')
def verify_footer_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    footer_links_amount = context.driver.find_element(*FOOTER_LINKS)
    assert len(footer_links_amount) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links_amount)}'



