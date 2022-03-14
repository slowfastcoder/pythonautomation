from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
import time
#variables
terms_url = "https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088"

#locators
PRIVACY_LOC = (By.XPATH, "//a[contains(@href,'privacy')]")

#locator on window2
HEADER_LOC = (By.XPATH, "//h1")

@given("Open Amazon T&C page")
def open_tc_page(context):
    context.driver.get(terms_url)

@when("Store original windows")
def store_windows(context):
    context.original_window = context.driver.window_handles[0]

@when("Click on Amazon Privacy Notice link")
def click_priv_link(context):
    context.driver.wait.until(EC.element_to_be_clickable(PRIVACY_LOC), message='privacy url not clickable').click()
    context.new_window = context.driver.window_handles[1]

@when("Switch to the newly opened window")
def switch_window(context):
    context.driver.switch_to.window(context.new_window)


@then("Verify Amazon Privacy Notice page is opened")
def verify_notice(context):
    expected_results = "Privacy Notice"
    y = context.driver.wait.until(EC.presence_of_element_located(HEADER_LOC), message='cannot find element')
    assert expected_results in y.text, 'test failed'

#I had to create 2 separate scenarios because it won't let me run another AND when there is a then.

@when("User can close and reopen original window")
def close_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)




