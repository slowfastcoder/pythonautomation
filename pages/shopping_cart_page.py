from selenium.webdriver.common.by import By

from pages.base_page import Page

class ShoppingCartPage(Page):
    #locators on main page
    CART_URL = (By.ID, "nav-cart")
    #locators for the shopping cart test page
    EXPECTED = (By.XPATH, "//h2")


    def click_cart(self):
        self.click(*self.CART_URL)

    def verify_emptyc(self):
        self.verify_partial_text("empty", *self.EXPECTED)
