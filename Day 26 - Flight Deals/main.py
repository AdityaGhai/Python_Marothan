from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime

data = DataManager()
sheet_data = data.sheet_data()

flight = FlightSearch()

notification = NotificationManager()

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

Starting_port = "LON"

for detail in sheet_data:
    #Searching for different flights
    final_flight = flight.flight_search(Starting_port,detail["iataCode"], start_date, end_date)
    #checking if gotten flight price is lower than sheet price.
    if final_flight.price < detail['lowestPrice']:
        #if yes then sending the sms to the mobile about the latest price.
        sms = notification.send_sms(price=final_flight.price, depart_city=final_flight.origin_city,
                                    depart_code=final_flight.origin_airport, arr_city=final_flight.destination_city,
                                    arr_code=final_flight.destination_airport, out_date=final_flight.out_date,
                                    inb_date=final_flight.return_date)

