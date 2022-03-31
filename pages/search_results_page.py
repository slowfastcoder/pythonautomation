from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    #locators for results page go here
    #locators might be different depending on which page your going to

    RESULT = (By.XPATH, "")
    PRODUCT_PRICE = (By.XPATH, "")
    DEPARTMENT = (By.CSS_SELECTOR, "#nav-subnav[data-category='books']")
    DEPARTMENT_MOBILE = (By.XPATH, "//div[@id='nav-subnav']//span")

    def verify_search_result(self, expected_result):
        self.verify_text(expected_result, *self.RESULT)

    def verify_correct_department(self):
        self.wait_for_element_appear(*self.DEPARTMENT)

#hw8
    def verify_correct_department2(self):
        self.wait_for_element_appear(*self.DEPARTMENT_MOBILE)
