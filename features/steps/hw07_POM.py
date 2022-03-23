from behave import given, when, then


@given('Open Amazon page')
def open_amazon_page(context):
    context.app.sign_in_page.open_url()

@when('Click Amazon Orders link')
def click_orders(context):
    context.app.sign_in_page.click_orders()

@then('Verify Sign In page is opened')
def verify_signin(context):
    context.app.sign_in_page.verify_signIn()


@when('Click on cart icon')
def click_cart(context):
    context.app.shopping_cart_page.click_cart()


@then("Verify 'Your Shopping Cart is empty.' text present")
def verify_empty_cart(context):
    context.app.shopping_cart_page.verify_emptyc()
