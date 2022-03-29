from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.ID, 'nav-orders')
    FLAG = (By.CSS_SELECTOR, ".icp-nav-flag.icp-nav-flag-us")
    SPANISH_LANG = (By.CSS_SELECTOR, "[href='#switch-lang=es_US']")
    SELECT_DEPARTMENT = (By.ID, 'searchDropdownBox')
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href='/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6']")
    DEALS_SHOWN = (By.CSS_SELECTOR, "div.nav-template.nav-flyout-content")

    def search_product(self, keyword):
        self.input_text(keyword, *self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.wait_for_element_click(*self.ORDERS)

    def hover_lang_options(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def select_department(self, alias: str):
        select_department = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(select_department)
        select.select_by_value(f'search-alias={alias}')

    def verify_spanish_lang_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_automotive(self):
        select_automitive = self.find_element(*self.SELECT_DEPARTMENT)

    def hover_department_options(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_deals_shown(self):
        self.wait_for_element_appear(*self.DEALS_SHOWN)