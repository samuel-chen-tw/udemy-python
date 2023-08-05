#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
import datetime
from notification_manager import NotificationManager
data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_data()
notification_manager = NotificationManager()

from pprint import pprint

if sheet_data[0]["iataCode"] == "":
    for data in sheet_data:
        data["iataCode"] = flight_search.get_destination_code(data["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_data()

date_from = datetime.datetime(2023, 9, 1)
date_to = datetime.datetime(2023, 12, 31)

for destination in sheet_data:
    flight = flight_search.check_flights(destination["iataCode"], date_from, date_to)

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message = f"Low price alert! Only TWD:{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}."
        )




