from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    #EMPTY_CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def search_product(self, keyword):
        self.input_text(keyword, *self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_BTN)

    def click_cart(self):
        self.click(*self.EMPTY_CART)
