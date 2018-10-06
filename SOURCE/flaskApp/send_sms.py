# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACad328f3a21f1b04309692b077108f197", "940cb68d1775d1f3ff1b087261d33f28")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+16313984501",
                       from_="+16312142113",
                       body="Thank you for your interest in SER Houston. blah blah blah")