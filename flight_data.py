import requests
from datetime import datetime,timedelta


class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self,iata_code,wanted_price,iatacode_departure):


        # aici ma ocup de data
        today = datetime.now()
        six_months = today + timedelta(days=6 * 30)
        one_week = today + timedelta(days=7)
        three_weeks = today + timedelta(days=28)

        today = today.strftime("%d/%m/%Y")
        six_months = six_months.strftime("%d/%m/%Y")


        apikey_flight = "s0h2Fu-KlYeJ_rNNrO7SNblqfkXcrJ0m"
        api_flight = "https://api.tequila.kiwi.com/v2/search"

        header = {
            "apikey": apikey_flight,
        }

        find_flight_param = {
            "fly_from": iatacode_departure,
            "fly_to": iata_code,
            "date_from": today,
            "date_to": six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        flight = requests.get(url=api_flight, headers=header, params=find_flight_param)
        flight.raise_for_status()


        #in cazul in care vrei sa vezi si ce zboruri nu sunt valabile, poti sa scoti comentariul de la exceptie

        try:
            self.departure_city=flight.json()["data"][0]["cityFrom"]
            self.arrival_city=flight.json()["data"][0]["cityTo"]
            self.price=flight.json()["data"][0]["price"]
            self.iataCode_departure=iatacode_departure
            self.iataCode_arrival=iata_code
            self.outbound_date=flight.json()["data"][0]["route"][0]["local_arrival"]

            #aici am scos niste caractere ce erau in plus ca sa fie citet rezultatul
            self.inbound_date=flight.json()["data"][0]["route"][0]["local_departure"].replace('T',' ')
            self.inbound_date=self.inbound_date.replace(':00.000Z','')


            self.avalible=True
            self.text =f'Flight avalible from {iatacode_departure} to {iata_code}.\n' \
                       f'Price: {self.price} {find_flight_param["curr"]}, targeted price: {wanted_price} {find_flight_param["curr"]}.\n' \
                       f'Departure city: {self.departure_city}, arrival city: {self.arrival_city}.\n' \
                       f'Inbound date: {self.inbound_date}.\n'

            # print(f'flight avalible from {IATACODE_DEPARTURE} to {iata_code} . '
            #       f'Price: {self.price}{find_flight_param["curr"]}, targeted price: {wanted_price}{find_flight_param["curr"]} ')

        except IndexError:
            # print(f"no flight from {IATACODE_DEPARTURE} to {iata_code}")
            self.avalible=False


