from data_manager import DataManager
from flight_search import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dm = DataManager()
fs = FlightSearch()

sheet_data = dm.get_destenations()

for place in sheet_data:
    if place["iataCode"] == "":
        iata_code = fs.iata_code()
        city_id = place["id"]
        dm.update_iata_codes(id=city_id, iata=iata_code)



print(sheet_data)