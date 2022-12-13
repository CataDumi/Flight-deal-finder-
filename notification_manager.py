from twilio.rest import Client
ACCOUNT_SID="AC088d29ca1bc21fc2908e13c933866c98"
AUTH_TOKEN="81e92b53f1b5aad76066d2b47e00b54e"

class NotificationManager:
    #asta e functionalitatea in plus . ea iti permite sa primesti un mesaj pe telefon in momentul in care
    # iti este gasit un zbor cu pretul mai mic decat cel pe care l am introdus
    def __init__(self,text):
        self.text=text

    def send_sms(self):
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            message = client.messages \
                .create(
                body=f"{self.text}",
                from_='+13466994983',
                to='+40753081636')



