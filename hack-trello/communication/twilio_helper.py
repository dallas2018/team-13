from json import load
from twilio.rest import Client

class TwilioHelper():
    '''
    Class that sends reminders to users via SMS using Twilio API
    '''
    def __init__(self):
        '''
        Default constructor
        '''
        with open("credentials.json") as f:
            creds = load(f)
        self.account_sid = creds["twilio"]["account_sid"]
        self.auth_token = creds["twilio"]["auth_token"]
        self.client = Client(self.account_sid, self.auth_token)
        self.numF = creds["twilio"]["number"] # Number that texts are sent from

    def text_user(self, message: str, numT: str) -> None:
        '''
        Texts user by taking in Trello to-do list and number to send to
        '''
        message = self.client.messages.create(body=message,to=numT, from_ = self.numF)
