from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class='a-row a-size-base a-color-base'] [class*='a-size-base a-link-normal'] [class='a-price'] [aria-hidden='true']")


    def verify_search_result(self, expected_result):
        self.verify_text(expected_result, *self.RESULT)

    def click_first_product(self):
        self.click(*self.PRODUCT_PRICE)