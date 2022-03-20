from pages.bestsellers_page import BestsellersPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.bestsellers_page = BestsellersPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)

'''        
a = Application()
a.header
a.main_page
'''