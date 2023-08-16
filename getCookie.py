import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os

chrome_options = uc.ChromeOptions()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("user_agent=DN")
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--user-data-dir')
chrome_options.add_argument('--allow-running-insecure-content')

secret_username = os.getenv('USER_EMAIL')
secret_password = os.getenv('USER_PASSWORD')

driver = uc.Chrome(options=chrome_options)
driver.delete_all_cookies()

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--window-size-1920,1080")

time.sleep(2)
driver.get(os.getenv('model_url'))
time.sleep(2)
driver.maximize_window()
time.sleep(3)
# enter sign in button
driver.get(os.getenv('BASE_URL'))

# SIGN IN EMAIL
time.sleep(2)
driver.switch_to.active_element.send_keys(secret_username)
time.sleep(2)

# press next
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]').click()
time.sleep(2)

# SIGN IN PASSWORD
driver.switch_to.active_element.send_keys(secret_password)
time.sleep(2)

# press next
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]').click()
time.sleep(2)

# GET COOKIES 
time.sleep(2)

print(driver.get_cookie("__Secure-1PSID"))
cookie = driver.get_cookie("__Secure-1PSID")

# standby
time.sleep(3)

doc = open("cookie.txt", "w")
doc.write((str(cookie['value'])))
print("cookie wrote")
doc.close()

time.sleep(2)

input('')
