import requests
from bs4 import BeautifulSoup
import smtplib

AMAZON_URL = your chosen product url
email = your email
password = your password

TARGET_PRICE = 500

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6"
}

response = requests.get(url=AMAZON_URL, headers=header)
amazon_text = response.text
soup = BeautifulSoup(amazon_text, "lxml")
price = soup.select("span .a-price-whole")
product_price = int(price[0].getText().strip("."))
# print(product_price)
product_title = soup.select("h1 #productTitle")[0].getText().strip()
# print(product_title)

if product_price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(email, password)
        mess_text = f"{product_title} is now {product_price}.\n{AMAZON_URL}"
        connection.sendmail(
            from_addr=email,
            to_addrs="adityaghai21@gmail.com",
            msg=mess_text
        )
