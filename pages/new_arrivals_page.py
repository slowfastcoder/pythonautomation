from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep


class NewArrivalsPage(Page):

    #locators
    NEW_ARRIVALS = By.XPATH, "//*[contains(text(),'New Arrivals')]"
    DEALS = By.XPATH, "//a[@class='mm-merch-panel']"
    ENTIRE_TEXT = By.XPATH, "//body" #I'm not sure how to grab that hoover over element so i'm using the entire body -_-

    def open_url2(self):
        #self.open_url(end_url='gp/product/B074TBCSC8')
        self.open_page(end_url='gp/product/B074TBCSC8')

    def hoover_New_Arrivals(self):
        y = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(y).perform()
        sleep(5)

    def verify_deals(self):
        self.verify_partial_text("Women", *self.ENTIRE_TEXT)


