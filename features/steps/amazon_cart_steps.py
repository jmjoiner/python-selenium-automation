from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@when('Clicks on the cart icon')
def cart_icon_click(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/cart/view.html?ref_=nav_cart']").click()


@then('Verifies that Your Amazon Cart is empty')
def verify_amazon_cart(context):
    context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")


