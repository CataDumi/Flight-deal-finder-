import requests


API_FLIGHT="https://api.tequila.kiwi.com/locations/query"
APIKEY_FLIGHT="s0h2Fu-KlYeJ_rNNrO7SNblqfkXcrJ0m"



class FlightSearch:

    #aici iau datele de pe site ul cu zboruri, mai precis preiau un json din care selectez ce ma intereseaza.

    def __init__(self,city):

        header = {
            "apikey": APIKEY_FLIGHT,
        }

        search_param = {
            "term": city,
            "location_types": "airport",
            "limit": 1
        }

        search_city = requests.get(url=API_FLIGHT, headers=header, params=search_param)
        search_city.raise_for_status()
        # pprint(search_city.json())
        self.item=search_city.json()["locations"][0]["code"]