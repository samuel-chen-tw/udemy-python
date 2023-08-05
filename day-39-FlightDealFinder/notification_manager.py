from twilio.rest import Client

TWILIO_SID = "AC6f1a98483002331f96b8eeceadd7ddd9"
TWILIO_AUTH_TOKEN = "50f3caf47a906980f3da4585ce87af33"
TWILIO_VIRTUAL_NUMBER = "+12184234625"
TWILIO_VERIFIED_NUMBER = "+886917611749"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body = message,
            from_= TWILIO_VIRTUAL_NUMBER,
            to= TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)