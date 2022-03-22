from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    EMPTY_CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")
    CART_BTN = (By.ID, "add-to-cart-button")
    CART_COUNT = (By.ID, "nav-cart-count")

    def cart_page(self):
        self.cart_page("//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def cart_btn(self):
        self.click(*self.CART_BTN)

    def verify_cart_count(self, number):
        self.verify_text(number, *self.CART_COUNT)
