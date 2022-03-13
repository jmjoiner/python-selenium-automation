from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    context.driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='help-service-content'] [class='help-content'] h1")))


@then('User can close new window and switch back to original')
def close_new_window(context):
    context.driver.close()
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)
