from selenium.webdriver.common.by import By
from selenium import webdriver


'''
HW 03 - AN Tran
HW Assigned - 2/13/22
Date submitted - 2/20/22

'''

#Todo find the most optimal locators for create account (registration page



#some notes - the url for create a new account was very long

amazonCreateAccUrl = "https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&";

# init driver
driverpath = "I:\\selenium python\\driver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverpath)
driver.maximize_window()

# open the url
driver.get(amazonCreateAccUrl)

##locators are here

nameLoc = By.ID, 'ap_customer_name'
emailLoc = By.ID, 'ap_email'
passLoc = By.ID, 'ap_password'
submitBtnLoc = By.ID, 'continue'
createFreeBizAccLoc = By.CSS_SELECTOR, '.a-icon.a-icon-touch-link'
termsofUseUrlLoc = By.XPATH, "//div[@id='legalTextRow']/a"  #[0] - conditions of use, [1] - Privacy notice
additionalBtnLoc = By.XPATH, "//div[@class='a-row']/a"  # [0] - first  button sign in with existing accont, [1] - create biz acc


#elements
yourNameEle = driver.find_element(By.ID, 'ap_customer_name')
emailEle = driver.find_element(By.ID, 'ap_email')
passEle = driver.find_element(By.ID, 'ap_password')
submitBtnEle = driver.find_element(By.ID, 'continue')


#todo Update a test case for support search using BDD
#see feature folder -help_search.feature and -help_search.py

#todo create test case using BDD that opens amazon.com and clicks on cart and verties that your cart is empty
#see feature folder -search_cart.py and search_cart.feature


























