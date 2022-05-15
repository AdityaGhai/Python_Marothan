import requests

SHEETY_ENDPOINT = Your SHEETY ENDPOINT

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __int__(self):
        self.destination = {}

    def sheet_data(self):
        response = requests.get(url=f"{SHEETY_ENDPOINT}/prices")
        self.destination = response.json()["prices"]

        return self.destination

    def sheet_update(self):
        for loc in self.destination:
            param = {
                "price":{
                    "iataCode": loc["iataCode"]
                }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/prices/{loc['id']}", json=param)
            print(response.text)

    def get_customer_email(self):
        response = requests.get(url=f"{SHEETY_ENDPOINT}/users")
        return response.json()['users']