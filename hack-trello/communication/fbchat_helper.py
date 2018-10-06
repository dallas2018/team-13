from json import load
from fbchat import Client
from fbchat.models import *

class FBChatHelper():
    def __init__(self):
        with open("credentials.json") as f:
            creds = load(f)
        self.email = creds['facebook']['email']
        self.password = creds['facebook']['password']

    def message_user(self, message, name):
        client = Client(self.email, self.password)
        user = client.searchForUsers(name)[0]
        client.send(Message(text = message), thread_id = user.uid, thread_type = ThreadType.USER)
        client.logout()
