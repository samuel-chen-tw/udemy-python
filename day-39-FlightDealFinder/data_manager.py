import requests

SHEETY_ENDPOINT = "https://api.sheety.co/4109f017e74c092056c932eaf5943d9c/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        data = requests.get(url=SHEETY_ENDPOINT).json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
