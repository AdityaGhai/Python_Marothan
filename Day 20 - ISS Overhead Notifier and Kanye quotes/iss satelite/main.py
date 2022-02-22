import requests
from datetime import datetime
import smtplib
import time

# set your location
MY_LAT = 28.704060
MY_LONG = 77.102493
EMAIL = "dummytest000111@gmail.com"
PASSWORD = "dummy123456"

def is_iss_overhead():
    # get the current iss satelite location
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True


def is_night():

    parameters ={
            "lat" : MY_LAT,
            "lng" : MY_LONG,
            "formatted" : 0
        }
    # checking the time of sunrise and sunset as satelites can only be visible at night
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = datetime.now()
    hour_now = time_now.hour

    if sunrise < hour_now <= sunset:
        return True

while True:
    time.sleep(60)
    # checking if satelite is visible then send mail.
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                 from_addr=EMAIL,
                 to_addrs=EMAIL,
                 msg="Subject:Look up?\n\nISS on the sky."
             )

