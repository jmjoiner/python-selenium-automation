from selenium.webdriver.common.by import By

from pages.base_page import Page

class MainPage(Page):
    ORDER_LINK_LOCATOR = (By.ID, 'nav-orders')


    def open_main(self):
        self.open_page()

    def orders_link(self):
        self.find_element(*self.ORDER_LINK_LOCATOR).click()