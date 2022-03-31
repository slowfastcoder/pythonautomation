from selenium.webdriver.common.by import By
from behave import given, when, then

'''
  Scenario: Hoover over New Arrivals and see the deals
    Given Open Random Amazon Page
    When Hoover New Arrivals
    Then Verify Deals Appear
'''

@given ('Open Random Amazon Page')
def open_page(context):
    context.app.new_arrivals_page.open_url2()

@when ('Hoover New Arrivals')
def hover_new_arrival(context):
    context.app.new_arrivals_page.hoover_New_Arrivals()


@then ('Verify Deals Appear')
def verify_deals(context):
    context.app.new_arrivals_page.verify_deals()


