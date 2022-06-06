import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Your internet provider promised speed
PROMISED_DOWN = 100.0
PROMISED_UP = 100.0

s = Service(Your path to webdriver)

TWITTER_EMAIL = Your email id
TWITTER_PASS = Your password
TWITTER_PHONE = Your phone no

SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login"

class InternetSpeedTwitterBot:

    def __init__(self, s):
        self.driver = webdriver.Chrome(service=s)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        # Checking current speed of your internet
        self.driver.get(SPEEDTEST_URL)
        start = self.driver.find_element(By.CLASS_NAME, "start-text")
        start.click()
        time.sleep(60)
        down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.up = up_speed
        self.down = float(down_speed)

    def tweet_at_provider(self):

        self.driver.get(TWITTER_URL)
        time.sleep(5)
        # Log In the twitter account
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(2)
        try:
            password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASS)
            password.send_keys(Keys.ENTER)
        # Checking if its asking for mobile no. or username
        except selenium.common.exceptions.NoSuchElementException:
            phone = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            phone.send_keys(TWITTER_PHONE)
            phone.send_keys(Keys.ENTER)
            time.sleep(2)
            password = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASS)
            password.send_keys(Keys.ENTER)

        time.sleep(3)

        # sending the tweet
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 100down/100up?"
        tweet.send_keys(message)
        time.sleep(1)
        tweet_send = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_send.click()

excitel = InternetSpeedTwitterBot(s)

speed = excitel.get_internet_speed()
# checking if your internet is providing less speed
if excitel.down < PROMISED_DOWN:
    tweet = excitel.tweet_at_provider()
    print("Your complaint has been send with twitter.")
else:
    print("Your Internet is working Fine.")
