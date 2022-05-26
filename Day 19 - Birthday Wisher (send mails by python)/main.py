##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas as pd

# setting date time
date = dt.datetime.now()
bday_day = (date.month, date.day)

email = your email
password = your password

# reading csv and formatting into list of dictionary
birth_date = pd.read_csv("birthdays.csv").to_dict(orient="records")

for bday in birth_date:
    #checking if its a birth day
    if bday_day == (bday["month"], bday["day"]):
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        # opens a template and update the name
        with open(file_path, "r+") as file:
            template = file.read()
            template = template.replace("[NAME]", bday["name"])

        # sending the mail to birthday person
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday\n\n{template}"
            )
