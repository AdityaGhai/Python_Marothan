from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("yourwebdriverpath")

SIMILAR_ACCOUNT = "https://www.instagram.com/yourgivenid"
USERNAME = your username
PASSWORD = your password

INSTA_LOGIN_URL = "https://www.instagram.com/accounts/login/"

class InstaFollower:

    def __init__(self, s):
        self.driver = webdriver.Chrome(service=s)

    def login(self):
        # Login in your instagram account
        self.driver.get(INSTA_LOGIN_URL)
        time.sleep(3)
        user = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user.send_keys(USERNAME)
        paswd = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        paswd.send_keys(PASSWORD)
        paswd.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        # finding your given account whose followers you want to follow
        self.driver.get(SIMILAR_ACCOUNT)
        time.sleep(6)
        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'followers')
        followers.click()
        time.sleep(4)
        # Clicking on the followers
        modal = self.driver.find_element(By.CLASS_NAME, '_aano')
        for i in range(10):
            # calling follow function to follow the peoples
            self.follow()
            #scrolling the followers popup window
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(4)


    def follow(self):
        # Following the followers
        follow_btn = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        for btn in follow_btn:
            try:
                # clicking on follow button
                btn.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                # clicking on cancel button if you have already followed the person
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
                cancel_button.click()

insta = InstaFollower(s)
insta.login()
insta.find_followers()
