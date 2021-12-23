from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver')


# Amazon logo:
driver.find_element(By.XPATH, "//a[@class='a-icon a-icon-logo']")


# Create Account:
driver.find_element(By.ID, "h1.a-spacing-small")


# Your name field:
driver.find_element(By.CSS_SELECTOR, ".a-input-text a-span12 auth-autofocus auth-required-field")


# Mobile number or Email:
driver.find_element(By.CSS_SELECTOR, ".a-input-text a-span12 a-spacing-micro auth-required-field auth-require-claim-validation")


# Password:
driver.find_element(By.CSS_SELECTOR, ".a-input-text a-span12 auth-required-field auth-require-fields-match auth-require-password-validation")
# Passwords must be at least 6 characters:
driver.find_element(By.XPATH, "//a[@class='a-alert-content']")


# Renter Password:
driver.find_element(By.XPATH, "//a[@class='.a-input-text a-span12 auth-required-field auth-require-fields-match']")


# Continue:
driver.find_element(By.ID, 'continue')


# Conditions of Use:
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use']")


# Privacy Notice:
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice']")


# Sign In:
driver.find_element(By.XPATH, "//a[@class='a-link-emphasis']")