import requests

SHEETY_ENDPOINT = "your sheety endpoint"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __int__(self):
        self.destination = {}

    def sheet_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        self.destination = response.json()["prices"]

        return self.destination

    def sheet_update(self):
        for loc in self.destination:
            param = {
                "price":{
                    "iataCode": loc["iataCode"]
                }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/{loc['id']}", json=param)
            print(response.text)
