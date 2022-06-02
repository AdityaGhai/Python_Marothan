import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

URL = "https://tinder.com/"
FB_EMAIL = Your Email
FB_PASS = Your Password

s = Service("/home/jaro/Development/chromedriver")

driver = webdriver.Chrome(service=s)

driver.get(URL)
time.sleep(3)
# Login Button
login_btn = driver.find_element(By.XPATH, '//*[@id="s1746966696"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login_btn.click()
time.sleep(2)

######################### FACEBOOK LOGIN ################################
try:
    fb_login = driver.find_element(By.XPATH, '//*[@id="s18585620"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
    fb_login.click()

except selenium.common.exceptions.NoSuchElementException:
    # If facebook option not shown click on more option
    more_option = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/button')
    more_option.click()
    time.sleep(1)
    fb_login = driver.find_element(By.XPATH, '//*[@id="s18585620"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
    fb_login.click()

time.sleep(2)

base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
# Switching the window
driver.switch_to.window(fb_window)

# Signing In the Facebook ID
fb_email = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
fb_email.send_keys(FB_EMAIL)
fb_pass = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
fb_pass.send_keys(FB_PASS)
fb_btn_login = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
fb_btn_login.click()

time.sleep(5)

# Switching back to base window
driver.switch_to.window(base_window)


########################## Accepting the pop-ups or cookies ############################
tinder_popup1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
tinder_popup1.click()

time.sleep(1)

tinder_popup2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]')
tinder_popup2.click()

tinder_popup3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
tinder_popup3.click()

time.sleep(8)

################################ Automating the Swipe ############################
while True:
    time.sleep(1)
    try:
        pop_up = driver.find_element(By.XPATH, '//*[@id="s18585620"]/div/div/div[2]/button[2]/span').click()

    except Exception as error:
        pass

    except ElementClickInterceptedException:
        driver.find_element(By.CSS_SELECTOR, ".itsAMatch a").click()

    finally:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
