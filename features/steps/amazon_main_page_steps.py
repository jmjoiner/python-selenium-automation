from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "td.navFooterDescItem a")
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip a.nav-action-button")
BS_LINK_OPTIONS = (By.CSS_SELECTOR, "div[class*='nav-tab-all_style_zg-tabs'] a")

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Search for {keyword}')
def search_product(context, keyword):
    context.app.header.search_product(keyword)
    context.app.header.click_search()


@when('Click search icon')
def click_search_icon(context):
   context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click Orders')
def click_orders(context):
    # context.driver.find_element(By.ID, 'nav-orders').click()
    context.app.main_page.orders_link()


@when('CLick Sign In from popup')
def click_sign_in(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), message='Sign In popup not clickable')
    e.click()


@when('Wait for {sec} sec')
def wait(context, sec):
    sleep(int(sec))


@when('Click on Best Sellers Link')
def click_best_sellers(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[id='nav-xshop'] a[href*='nav_cs_bestsellers']").click()


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


@then('Verify that SignIn popup shown')
def verify_signin_popup(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_BTN), message='SignIn btn not visible')


@then('Verify that SignIn btn is clickable')
def verify_signin_popup_btn_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), message='SignIn btn not clickable')


@then('Verify that SignIn popup disappears')
def verify_signin_popup_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_BTN), message='SignIn btn still visible')


@then('Verify that user is on the Best Sellers Page')
def verify_bestsellers_page(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/bestsellers/'), message='BestSellers did not open')


@then('Verify user can click through Best Seller Links')
def verify_bestsellers_links(context):
    expected_links = ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']
    length = len(expected_links)

    for i in range(length):
        context.driver.find_elements(*BS_LINK_OPTIONS)[i].click()