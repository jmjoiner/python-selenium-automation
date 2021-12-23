from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@given('Open Amazon customer help page')
def open_amazon_customer_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Look for cancel order in help search')
def look_for_cancel_order(context):
    searchbar = context.driver.find_element(By.ID, "helpsearch")
    searchbar.send_keys('Cancel Order')
    searchbar.send_keys(Keys.ENTER)


@then('Verify Cancel order')
def verify_cancel_order(context):
    new_test = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    assert new_test == "Cancel Items or Orders", 'Never Happened'

