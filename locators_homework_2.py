from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver')

# By XPATH, Amazon Logo
driver.find_element(By.XPATH, "//a[@class='a-icon a-icon-logo']")

# By ID, Continue Button
driver.find_element(By.ID, "continue")

# By XPATH, multipule attributes
driver.find_element(By.XPATH, "//a[@class='a-expander-prompt']")

# By ID, Forgot password link
driver.find_element(By.ID, "auth-fpp-link-bottom")

# By ID, Other issues with sign-in link
driver.find_element(By.ID, "ap-other-signin-issues-link")

# By ID, Create your Amazon account Button
driver.find_element(By.ID, "createAccountSubmit")

# By XPATH, Conditions of use link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# By XPATH, Privacy Notice link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")

