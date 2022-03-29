from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class='a-row a-size-base a-color-base'] [class*='a-size-base a-link-normal'] [class='a-price'] [aria-hidden='true']")
    DEPARTMENT = (By.CSS_SELECTOR, '#nav-subnav[data-category="{DEPARTMENT_CATEGORY}"]')

    def get_department_locator(self, department: str):
        return [self.DEPARTMENT[0], self.DEPARTMENT[1].replace('{DEPARTMENT_CATEGORY}', department)]

    def verify_search_result(self, expected_result):
        self.verify_text(expected_result, *self.RESULT)

    def click_first_product(self):
        self.click(*self.PRODUCT_PRICE)

    def verify_correct_department(self, department):
        locator = self.get_department_locator(department)
        print(locator)
        self.wait_for_element_appear(*self.get_department_locator(department))