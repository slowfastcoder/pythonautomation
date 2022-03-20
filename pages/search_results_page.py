from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    #locators for results page go here
    #locators might be different depending on which page your going to

    RESULT = (By.XPATH, "")
    PRODUCT_PRICE = (By.XPATH, "")

    def verify_search_result(self, expected_result):
        self.verify_text(expected_result, *self.RESULT)