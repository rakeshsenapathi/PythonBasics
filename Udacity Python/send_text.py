from twilio.rest import TwilioRestClient
# Account Sid and Auth_id from twilio.com/user/account

account_sid = "AChjds"
auth_token = "cc692bb6079d4440dssad"

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
        body="Hi",
        to="999999",  # The number you wish to send to
        from_="99999")  # Your twilio Acc number

print(message.sid)
