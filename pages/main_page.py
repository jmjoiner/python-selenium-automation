from selenium.webdriver.common.by import By

from pages.base_page import Page

class MainPage(Page):
    ORDER_LINK_LOCATOR = (By.ID, 'nav-orders')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')

    def open_main(self):
        self.open_page()

    def orders_link(self):
        self.find_element(*self.ORDER_LINK_LOCATOR).click()

    def add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART_BTN)