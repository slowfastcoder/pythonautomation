from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



# init driver
driverpath = "I:\\selenium python\\driver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverpath)
driver.maximize_window()

# open the url
url1 = "https://www.amazon.com/"
url2 = "https://www.amazon.com/gp/help/customer/display.html"
url3 = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
driver.get(url3)

#signinBTn = driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']")
#hover = ActionChains(driver).move_to_element(signinBTn)
#hover.perform()
#signinBTn2 = driver.find_element(By.XPATH, "//*[text()='Sign in']")
#signinBTn2[1].Click()
#

AmazonLogoXpath = "//*[@class='a-icon a-icon-logo']"
emailFieldId = "ap_email"
conBtnId = "continue"
needHelpClass = "a-expander-prompt"
forgotPwXPath = "//*[contains(text(), 'Forgot your password')]"
otherIssueXPath = "//*[contains(text(), 'Other Issues')]"
createAccBtnId = "createAccountSubmit"
conditionsLinkXpath = "//*[contains(text(), 'Conditions of Use')]"
privacyNotice = "//*[contains(text(), 'Privacy')]"
helpLink = "//*[contains(text(), 'Help')]"



element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Email or mobile phone number')]")))

print("Nav to login page success")


sleep(1000)
driver.quit()

# todo - Create test cases for, help search,
# todo - Not required but you can try it out to learn - BDD test cases for logging out




