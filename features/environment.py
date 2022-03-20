from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from app.application import Application
from selenium.webdriver.support import expected_conditions as EC



def browser_init(context):
    """
    :param context: Behave context
    """


    driverpath = "I:\\selenium python\\driver\\chromedriverv99.exe"
    context.driver = webdriver.Chrome(executable_path=driverpath)

    #context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
