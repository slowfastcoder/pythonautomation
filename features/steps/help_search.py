from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep

#locators go here
SEARCH_INPUT = (By.CSS_SELECTOR, 'input#helpsearch')
SEARCH_SUBMIT = (By.NAME, 'btnK')
ACTUAL_RESULT = (By.XPATH, "//div[@class='help-content']/h1")

#urls and other variables
helpURL = "https://www.amazon.com/gp/help/customer/display.html"

@given('Open Amazon Help Page')
def open_google(context):
    context.driver.get(helpURL)


@when('Input {search_word} into help search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


#There is no submit button, so just send keys ENTER
@when('Press Enter on Search Field')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_INPUT).click()
    context.driver.find_element(*SEARCH_INPUT).send_keys(Keys.ENTER)
    sleep(2)


@then('Help results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    actual = context.driver.find_element(*ACTUAL_RESULT).text
    assert search_word.lower() in actual.lower(), f"Expected query not in {actual.lower()}"
    #assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"

