from selenium.webdriver.common.by import By
from pages.base_page import Page


class BestSellersPage(Page):
    TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    HEADER = (By.CSS_SELECTOR, '#zg_header_texrt')


    def open_amazon_bestsellers(self):
        self.open_url(end_url='gp/bestsellers/')

    def click_thru_top(self):
        top_links = self.driver.find_elements(*self.TOP_LINKS)

        for x in range(len(top_links)):
            link_to_click = self.driver.find_elements(*self.TOP_LINKS)[x]
            link_text = link_to_click.text
            link_to_click.click()
            self.verify_partial_text(link_text, self.HEADER)