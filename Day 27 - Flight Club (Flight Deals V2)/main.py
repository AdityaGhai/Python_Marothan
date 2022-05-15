from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime


Starting_port = "LON"

data = DataManager()
flight = FlightSearch()
notification = NotificationManager()

sheet_data = data.sheet_data()
customer_email = data.get_customer_email()
# print(customer_email)

#checking if iatacode is empty. if yes then update the code
if sheet_data[0]["iataCode"] == "":

    for city in sheet_data:
        city['iataCode'] = flight.iata_code(city['city'])
    # print(sheet_data)
    data.destination = sheet_data
    data.sheet_update()

# print(sheet_data)

#Setting the flight departion and return duration.
x = datetime.datetime.now() + datetime.timedelta(days=1)
start_date = x.strftime("%d/%m/%Y")
y = x + datetime.timedelta(days=180)
end_date = y.strftime("%d/%m/%Y")


for detail in sheet_data:
    #Searching for different flights
    final_flight = flight.flight_search(Starting_port,detail["iataCode"], start_date, end_date)

    if final_flight is None:
        continue
    # checking if gotten flight price is lower than sheet price.
    if final_flight.price < detail['lowestPrice']:
        #if yes then sending the sms to the mobile about the latest price.
        message_text = f"Low price alert! Only ₹{final_flight.price} to fly from {final_flight.origin_city}-" \
                       f"{final_flight.origin_airport} to {final_flight.destination_city}-" \
                       f"{final_flight.destination_airport}," \
                       f"from {final_flight.out_date} to {final_flight.return_date}."

        if final_flight.stop_overs >0:
            message_text += f"\nFlight has {final_flight.stop_overs} stop over, via {final_flight.via_city}"

        # sms = notification.send_sms(message_text)
            print(message_text)
        for email in customer_email:
            email_text= f"Subject:New Flight Deal\n\n{message_text}"
            notification.send_email(reciever=email["email"], text=email_text)
