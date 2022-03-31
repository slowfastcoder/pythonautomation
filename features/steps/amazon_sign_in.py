from behave import given, when, then

#lecture 7 notes
#i wrote the sign in page in file: hw07_POM.py

@when('Click on button from SignIn popup')
def click_pop_button(context):
    context.app.sign_in_page.click_orders()