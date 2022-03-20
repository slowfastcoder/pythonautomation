from pages.base_page import Page
from selenium.webdriver.common.by import By


class BestsellersPage(Page):

    #locators
    TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    HEADER = (By. CSS_SELECTOR, '#zg_banner_text')


    ActualURLList = (By.XPATH, "//*[contains(@class, '_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq')]//a")
    ACTUAL_RESULT = (By.XPATH, "//h2")
    PRODUCTLIST = (By.XPATH, "//div[@class='zg-carousel-general-faceout']")
    ADDCARTBTN = (By.ID, "add-to-cart-button")
    VIEWCARTBTN = (By.ID, "nav-cart-count")
    CART_ACTUALRESULT = (By.ID, "sc-subtotal-label-activecart")

    def open_amazon_bestsellers(self):
        self.open_url(end_url='gp/bestsellers/')

    def click_thru_top(self):
        top_links = self.driver.find_elements(*self.TOP_LINKS)

        for x in range(len(top_links)):
            link_to_click = self.driver.find_elements(*self.TOP_LINKS)[x]
            link_text = link_to_click.text
            link_to_click.click()
            #new_text = self.driver.find_element(*self.HEADER).text
            #assert link_text in new_text , f'Expected {link_text} to be in {new_text}'
            self.verify_partial_text(link_text, *self.HEADER)


