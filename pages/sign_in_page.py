from selenium.webdriver.common.by import By

from pages.base_page import Page

class SignInPage(Page):
    #locators go here
    order_link = (By.ID, "nav-orders")
    expected_loc = (By.XPATH, "//h1")




    #signed out users see sign in page when click on orders
    def open_orders(self):
        self.open_url(end_url='orders/')

    def open_amazon(self):
        self.open_url()

    def click_orders(self):
        self.click(*self.order_link)

    def verify_signIn(self):
        self.verify_text("Sign-In", *self.expected_loc)