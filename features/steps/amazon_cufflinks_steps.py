from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from features.steps.product_search import SEARCH_SUBMIT


@when('Search for cufflinks')
def search_amazon_cufflinks(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('cufflinks')


@then('Search result have {expected_result}')
def results_have_cufflinks(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "span.a-color-state.a-text-bold").text
    assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_result}'

