from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.logger import logger

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://amazon.com/"
        self.wait = driver.wait = WebDriverWait(driver, 10) #wait 10 seconds

    def open_url(self, end_url: str = ''):
        #implement loggers
        logger.info(f'Opening {self.base_url}{end_url}...')
        self.driver.get(f'{self.base_url}{end_url}')
    #def input_text(self, *locator, text): #notes - this will give error, put the asterisk before any arguments (text)

    def open_page(self, end_url=''):
        print(f'{self.base_url}{end_url}')
        logger.info(f'Opening {self.base_url}{end_url}...')
        self.driver.get(f'{self.base_url}{end_url}')


    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)


    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_for_element_click(self, *locator):
        e = self.wait.until((EC.element_to_be_clickable(locator)))
        e.click()
    #lesson 8 new base methods
    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))


    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected text {expected_text} did not match {actual_text}"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, \
            f"Expected text {expected_text} did not match {actual_text}"



#p = Page()
#p.driver

