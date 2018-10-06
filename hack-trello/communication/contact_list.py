from json import load
import os

class ContactList():
    '''
    Class that forms the contact list to send reminders to
    '''
    def __init__(self):
        '''
        Default constructor
        '''
        with open('contacts.json') as f:
            self.contacts = load(f)

