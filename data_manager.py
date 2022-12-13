import requests
update_endpoint="https://api.sheety.co/5711733d27121472f46caee0bb743eef/copyOfFlightDeals/prices/[Object ID]"

class DataManager:

    ### aici preiau datele din google sheet-ul meu

    def __init__(self,id,code):
        body = {
            "price": {
                "iataCode": code
            }
        }
        update = requests.put(
            url=f"https://api.sheety.co/5711733d27121472f46caee0bb743eef/copyOfFlightDeals/prices/{id}",
            json=body)
        update.raise_for_status()
