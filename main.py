import requests
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData

sheety_read_endpoint="https://api.sheety.co/5711733d27121472f46caee0bb743eef/copyOfFlightDeals/prices"
iata_code_input=input('Type a valid iata code. (e.g. OTP / VIE )\n').upper()

read=requests.get(url=sheety_read_endpoint)
read.raise_for_status()
# pprint(read.json())

data_sheet=read.json()["prices"]
# pprint(data_sheet)

for item in data_sheet: ##pana aici inclusiv for e bn ...
    # aici completez in sheet ul meu pt fiecare aeroport care nu are un iata cod, il adaug eu

    if len(item["iataCode"])==0:
        item["iataCode"]=FlightSearch(item["city"]).item
        data=DataManager(id=item['id'],code=item["iataCode"])


    flight=FlightData(item["iataCode"],wanted_price=item["lowestPrice"],iatacode_departure=iata_code_input)
    if flight.avalible == True:
        print(flight.text)

  # partea de sms - aici imi trimit sms pe telefon daca este vren zobor disponibil care indeplineste toate cerintele necesare
  #       sms=NotificationManager(text=flight.text)
  #       sms.send_sms()




