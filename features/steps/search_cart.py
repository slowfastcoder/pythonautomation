from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep
import unittest

#locators go here
CART_ICON = (By.ID, 'nav-cart')
ACTUAL_RESULT = (By.XPATH, "//h2")

#urls and other variables
mainURL = "https://www.amazon.com/"

@given('Open Amazon Main Page')
def open_google(context):
    context.driver.get(mainURL)

@when('User clicks on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()

@then ('An Empty Cart result should be shown')
def verify_empty_cart(context):
    expectedResult = "Your Amazon Cart is empty"
    actual = context.driver.find_element(*ACTUAL_RESULT)
    print(actual.text)
    assert (expectedResult == actual.text)


