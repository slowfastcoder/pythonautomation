from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')

@given('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when ('Search for {keyword}}')
def search_product(context):
    context.driver.find_element(*SEARCH_INPUT).send_keys(keyword)
    context.driver.find_element(*SEARCH_BTN).click()


@then ('Verify search results are shown')
def verify_result(context):
    pass