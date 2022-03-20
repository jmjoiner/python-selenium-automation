from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    EMPTY_CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def cart_page(self):
        self.cart_page("//div[@class='a-row sc-your-amazon-cart-is-empty']")