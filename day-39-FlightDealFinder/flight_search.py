import requests
from flight_data import FlightData

LOCATION_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "3Dj9p7KRNGkdR-jmFT5IMP5R4Krsrf9d"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        headers = {"apikey": TEQUILA_API_KEY}
        params = {"term": city_name, "location_types": "city"}
        response = requests.get(url=f"{LOCATION_ENDPOINT}/locations/query", params=params, headers=headers)
        print(response.json())
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, fly_to_city_code, date_from, date_to):
        headers = {"apikey": TEQUILA_API_KEY}
        params = {
            "fly_from": "TPE",
            "fly_to": fly_to_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 7,
            "one_for_city": 0,
            "adults": 2,
            "max_stopovers": 0,
            "curr": "TWD"
        }
        response = requests.get(url=f"{LOCATION_ENDPOINT}/search", params=params, headers=headers)

        try:
            data = response.json()["data"][0]
            print(data)
        except IndexError:
            print(f"No flights found for {fly_to_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            # out_date=data["route"][0]["local_departure"].split("T")[0],
            # return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: TWD {flight_data.price}")
        return flight_data

