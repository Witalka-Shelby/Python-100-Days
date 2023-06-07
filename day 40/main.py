from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

FLY_FROM = "FRA"


dm = DataManager()
fs = FlightSearch()
fd = FlightData()

sheet_data = dm.get_destenations()

# updates the missing IATA codes
for place in sheet_data:
    city_id = place["id"]
    city_name = place["city"]
    iata_code = place["iataCode"]
    lowest_price = place["lowestPrice"]

    if iata_code == "":
        iata_code = fs.iata_code(city_name)
        dm.update_iata_codes(id=city_id, iata=iata_code)

    cheap_flight = fd.search_fligh(departure_airport_code=FLY_FROM, fly_to=iata_code, lowest_price=lowest_price)

    if cheap_flight == None:
        continue
    
    # send notification
    NotificationManager(cheap_flight)

