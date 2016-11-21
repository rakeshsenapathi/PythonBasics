from twilio.rest import TwilioRestClient
# Account Sid and Auth_id from twilio.com/user/account

account_sid = "AC34c41a1108759eb23f6f630147c555d6"
auth_token = "cc692bb6079d44405e096b64dc4815dc"

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
        body="Hi",
        to="+91 9052769653",  # The number you wish to send to
        from_="+37258821528")  # Your twilio Acc number

print(message.sid)
