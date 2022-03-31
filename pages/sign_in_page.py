from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
#extra code from lesson 8 starts
    def verify_sign_in_opened(self):
        self.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'), message = "wrong url")
