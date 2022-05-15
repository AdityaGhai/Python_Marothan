from twilio.rest import Client
import smtplib

twi_sid = your twilio sid
twi_token = your twilio token

email = your email id
password = your email password

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self,text):
        client = Client(twi_sid, twi_token)

        message_text = text

        message = client.messages.create(
            body=message_text,
            from_=your virtual no.,
            to=your verified no.
        )
        print(message.sid)

    def send_email(self, reciever, text):
        print("Sending Mail")
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=email,password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=reciever,
                msg=text.encode("utf-8")
            )
