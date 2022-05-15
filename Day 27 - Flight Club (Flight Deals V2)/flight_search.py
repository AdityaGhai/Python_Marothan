import requests
from flight_data import FlightData
from pprint import pprint

TEQ_ENDPOINT = Your Tequila endpoint
TEQ_API_KEY = Your api key token




class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def iata_code(self, data):
        headers = {
            "apikey": TEQ_API_KEY
        }
        data_param = {
            "term": data,
            "location_types": "city"
        }
        respone = requests.get(url=f"{TEQ_ENDPOINT}/locations/query",headers=headers,params=data_param)
        result = respone.json()["locations"][0]["code"]
        return result

    def flight_search(self, Starting_port, Dest_port, start_date, end_date):
        flight_param = {
            "fly_from": Starting_port,
            "fly_to": Dest_port,
            "date_from": start_date,
            "date_to": end_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"

        }
        api_header = {
            "apikey": TEQ_API_KEY
        }
        response = requests.get(url=f"{TEQ_ENDPOINT}/v2/search", headers=api_header, params=flight_param)
        try:
            flight_data = response.json()["data"][0]
            # pprint(flight_data)
        except IndexError:
            # print(f"No flights found for {Dest_port}.")
            flight_param['max_stopovers']= 2
            new_response = requests.get(url=f"{TEQ_ENDPOINT}/v2/search", headers=api_header, params=flight_param)
            try:
                flight_data = new_response.json()['data'][0]

            except IndexError:
                return None

            else:
                flight_info = FlightData(price=flight_data['price'],
                                         origin_city=flight_data["route"][0]['cityFrom'],
                                         origin_airport=flight_data["route"][0]['cityCodeFrom'],
                                         destination_city=flight_data["route"][0]['cityTo'],
                                         destination_airport=flight_data["route"][0]['cityCodeTo'],
                                         out_date=flight_data["route"][0]['local_departure'].split("T")[0],
                                         return_date=flight_data["route"][1]['local_departure'].split("T")[0],
                                         stop_overs=1,
                                         via_city=flight_data["route"][0]['cityTo'])
                return flight_info

        else:
            flight_info = FlightData(price=flight_data['price'],
                                     origin_city=flight_data["route"][0]['cityFrom'],
                                     origin_airport=flight_data["route"][0]['cityCodeFrom'],
                                     destination_city=flight_data["route"][0]['cityTo'],
                                     destination_airport=flight_data["route"][0]['cityCodeTo'],
                                     out_date=flight_data["route"][0]['local_departure'].split("T")[0],
                                     return_date=flight_data["route"][1]['local_departure'].split("T")[0],
                                     )

            # print(f"{flight_info.destination_city}:₹{flight_info.price}")
            return flight_info
