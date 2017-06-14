import os
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "XXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18045551212",
    from_="+18045551212",
    body="Thanks for your order!  On a scale of 1-10 would you recommend Snagajob to a friend?  Reply with the number 1 to 10 to this message.")

print(message.sid)
