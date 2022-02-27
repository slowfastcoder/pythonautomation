from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep
import unittest

#locators go here
ActualURLList = (By.XPATH, "//*[contains(@class, '_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq')]//a")
ACTUAL_RESULT = (By.XPATH, "//h2")
PRODUCTLIST = (By.XPATH, "//div[@class='zg-carousel-general-faceout']")
ADDCARTBTN = (By.ID, "add-to-cart-button")
VIEWCARTBTN = (By.ID, "nav-cart-count")
CART_ACTUALRESULT = (By.ID, "sc-subtotal-label-activecart")

#urls and other variables
mainURL = "https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers"
expectedResult = 5


@given('User goes to amazon best seller')
def navigate_BestSeller(context):
    context.driver.get(mainURL)


@then('There should be {expectedNumber} links present')
def verify_links(context, expectedNumber):
    actualResults = context.driver.find_elements(*ActualURLList)
    print(str(len(actualResults)) + " " + str(expectedNumber))

    assert len(actualResults) == int(expectedNumber)
    print("Test passed")



@when('User clicks {product_num} product to view')
def add_cart(context, product_num):
    context.driver.find_elements(*PRODUCTLIST)[int(product_num)].click()

@when('Adds that product to the cart')
def add_cart(context):
    context.driver.find_element(*ADDCARTBTN).click()


@when('User navigates to view the cart page')
def add_cart(context):
    context.driver.find_element(*VIEWCARTBTN).click()


@then('There should be {expectedItem} item in the cart')
def add_cart(context, expectedItem):
    actual = context.driver.find_element(*CART_ACTUALRESULT).text
    print(actual + (expectedItem))
    assert (expectedItem) in actual

