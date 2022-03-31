from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep

from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    # hw8 locators
    LANGUAGE_BUTTON = (By.XPATH, "//*[@class='icp-nav-link-inner']")
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us')
    FLAG3 = (By.CSS_SELECTOR, '.nav-line-2')
    FLAG2 = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By. CSS_SELECTOR, "[href='#switch-lang=es_US']")
    SELECT_DEPARTMENTID = (By.ID, "searchDropdownBox")
    SELECT_DEPARTMENT = (By.XPATH, "//select[@id='searchDropdownBox']/option")

    searchalias = "search-alias=software"
    searchalias2 = "search-alias=stripbooks"

    def open_main(self):
        #self.open_url('https://www.amazon.com')
        self.open_url()

    def hover_language(self):
        #element not found issue, it is hoovering over the sign in instead
        #it's not working on my browser.
        flag = self.find_element(*self.FLAG2)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag).perform()
        sleep(5)

    def verify_spanish(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_departments(self):
        sleep(5)
        #AttributeError: 'NoneType' object has no attribute 'tag_name'
        # figure out why it's not picking up the element later....
        select_department = self.find_element(*self.SELECT_DEPARTMENTID) #can't find select
        select = Select(select_department)
        all_selected_options = select.all_selected_options
        print(all_selected_options)
        select.select_by_value('search-alias=stripbooks')


    def select_dropdown(self):
        select_drop = self.find_element(*self.SELECT_DEPARTMENTID)
        select = Select(select_drop)
        select.select_by_value("search-alias=mobile")
        #for x in select_drop:
        #    print(x.Text)

    def search(self, item):
        pass

    def click_search_icon(self):
        pass

    def verify_books(self):
        pass