from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2a6cae5a5d3b26c7fbbb57fc327469f4"
# Your Auth Token from twilio.com/console
auth_token  = "d81a3d84605d75cef24f70649577a4bb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12136047704",
    from_="+14243583569",
    body="Hello from Python!")

print(message.sid)
