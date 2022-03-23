from pages.bestsellers_page import BestsellersPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.shopping_cart_page import ShoppingCartPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.sign_in_page = SignInPage(self.driver)
        self.bestsellers_page = BestsellersPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)

'''        
a = Application()
a.header
a.main_page
'''