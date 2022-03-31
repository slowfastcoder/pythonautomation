from selenium.webdriver.common.by import By
from behave import given, when, then


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')

#Hw 5 - loops
product_url01 = "https://www.amazon.com/Dickies-Heavyweight-Sleeve-Big-tall-2X-Large/dp/B00B6EDAS8/ref=sr_1_7?crid=3FJOPF0AMT2W9&keywords=shirts&qid=1647156119&sprefix=shirt%2Caps%2C143&sr=8-7"
COLOR_LIST = (By.XPATH, "//*[contains(@id,'color_name_')]")
SELECTED_COLOR = (By.XPATH, "//div[@id='variation_color_name']/div/span")


@given('Open Amazon')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com')
    context.app.main_page.open_main()

@when ('Search for {keyword}')
def search_product(context, keyword):
    #context.driver.find_element(*SEARCH_INPUT).send_keys(keyword)
    #context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_product(keyword)
    context.app.header.click_search()


@then ('Verify search results are shown for {keyword}')
def verify_result(context, keyword):
    #pass
    context.app.search_results_page.verify_search_result(keyword)

@given('Navigate to Product Page')
def nav_product(context):
    context.driver.get(product_url01)

@when("Sort through Color")
def sort_color(context):
    context.colors = context.driver.find_elements(*COLOR_LIST)
    for x in context.colors:
        #x.click()
        print(x.get_attribute("title")[16:30])


@then("Verify color selected")
def verify_color(context):
    #expected_colors = []
    context.selected_colors = context.driver.find_elements(*SELECTED_COLOR)
    for x in context.colors:
        for y in context.selected_colors:
            x.click()
            #print(x.get_attribute("title"))
            #print(y.text)
            #sometimes error because clicking too fast
            assert (x.get_attribute("title")[16:30]) in y.text

@when("Hover over language options")
def hover_language(context):
    context.app.main_page.hover_language()

@then("Verify Spanish option present")
def verify_spanish(context):
    context.app.main_page.verify_spanish()

#lesson 8 notes

@when("Select books department")
def select_departments(context):
    context.app.main_page.select_departments()

@then("Verify books department is selected")
def verify_books(context):
    context.app.search_results_page.verify_correct_department()

@when ("Select Dropdown")
def select_dropdown(context):
    context.app.main_page.select_dropdown()

@then("Verify Mobile department is selected")
def verify_books(context):
    context.app.search_results_page.verify_correct_department2()
