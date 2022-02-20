from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get('https://www.amazon.com/gp/help/customer/display.html')

searchbar = driver.find_element(By.ID, "helpsearch")
searchbar.send_keys('Cancel Order', Keys.ENTER)


new_test = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
assert new_test == "Cancel Items or Orders", 'Never Happened'

driver.quit()