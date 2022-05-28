from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service(Your driver path)
timeout = time.time() + 5
five_min = time.time() + 60*5

#setting up chrome drivers
browser = webdriver.Chrome(service=s)
browser.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = browser.find_element(By.ID, "cookie")


items = browser.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()
    #buying upgrades in every 5 seconds
    if time.time() > timeout:
        # all prices of upgrades
        prices_all = browser.find_elements(By.CSS_SELECTOR, "#store div b")
        all_price = []
        for price in prices_all:
            if price.text != "":
                price = int(price.text.split("-")[1].strip().replace(",", ""))
                all_price.append(price)

        # print(all_price)
        # total upgrades available
        upgrades ={}
        for n in range(len(all_price)):
            upgrades[all_price[n]] = item_ids[n]
        # print(upgrades)

        # Money we have to buy upgrades
        money = browser.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        #affordable upgrades we have
        affordable_up = {}
        for cost,id in upgrades.items():
            if cookie_count > cost:
                affordable_up[cost] = id
        print(affordable_up)
        best_upgrade = max(affordable_up)
        purchase_id = affordable_up[best_upgrade]

        # purchasing the upgrades
        buy = browser.find_element(By.ID, purchase_id)
        buy.click()

        # updating the timeout
        timeout = time.time() + 5

        # checking for 5 minutes and printing cps of bot.
        if time.time() > five_min:
            cps = browser.find_element(By.ID, "cps")
            print(cps.text)
            break
