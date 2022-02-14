from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# init driver
driverpath = "I:\\selenium python\\driver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverpath)
driver.maximize_window()

# todo - Create test cases for, help search,
# todo - Not required but you can try it out to learn - BDD test cases for logging out

# open the url
url1 = "https://www.amazon.com/"
url2 = "https://www.amazon.com/gp/help/customer/display.html"
sign_in_url3 = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"

driver.get(url2)

#1 - xpath and id for locators
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


searchBox = driver.find_element(By.ID, "helpsearch")
searchBox.click()
searchBox.send_keys("Cancel order")
searchBox.send_keys(Keys.ENTER)

actualResult = driver.find_element(By.XPATH, "//div[@class='help-content']/h1")
print(actualResult.text)

assert 'Cancel Items' in actualResult.text
print('Test Passed')

driver.quit()






