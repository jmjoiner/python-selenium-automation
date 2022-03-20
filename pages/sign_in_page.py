from selenium.webdriver.common.by import By

from pages.base_page import Page

class SignInPage(Page):
    def verify_sign_in_page(self):
        # assert "https://www.amazon.com/ap/signin" in self.driver.current_url, \
        #     f'https://www.amazon.com/ap/signin not in {self.driver.current_url}'
        self.verify_url_contains_query("https://www.amazon.com/ap/signin")