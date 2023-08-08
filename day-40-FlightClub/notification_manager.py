from twilio.rest import Client
import smtplib

TWILIO_SID = "AC6f1a98483002331f96b8eeceadd7ddd9"
TWILIO_AUTH_TOKEN = "50f3caf47a906980f3da4585ce87af33"
TWILIO_VIRTUAL_NUMBER = "+12184234625"
TWILIO_VERIFIED_NUMBER = "+886917611749"

EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "samuel811215@gmail.com"
MY_PASSWORD = "zrcusgixpsqhgwul"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )