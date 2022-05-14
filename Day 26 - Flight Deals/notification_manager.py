from twilio.rest import Client

twi_sid = "your twilio accoutn sid"
twi_token = "your token"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, price, depart_city, depart_code, arr_city, arr_code, out_date, inb_date):
        client = Client(twi_sid, twi_token)

        message_text = f"Low price alert! Only ₹{price} to fly from {depart_city}-{depart_code} to {arr_city}-{arr_code}," \
                  f"from {out_date} to {inb_date}."

        message = client.messages.create(
            body=message_text,
            from_="your twilio virtual no.",
            to='your registered no.'
        )
        print(message.sid)