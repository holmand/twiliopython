from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "XXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18045551212",
    from_="+18045551212",
    body="You have just been added to the schedule.  Do you want to see a copy of the schedule?")

print(message.sid)
