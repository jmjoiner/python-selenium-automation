from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then


@then('Verify blog is opened')
def verify_blog_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/'))


@then('Close blog')
def close_blog(context):
    context.driver.close()
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)


