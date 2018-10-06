from .contact_list import ContactList
from .twilio_helper import TwilioHelper
from .sendgrid_helper import SendGridHelper
from .fbchat_helper import FBChatHelper
from time import sleep

# Forming path to trello_helper module as it is outside with working directory
import sys, os
sys.path.append(os.path.abspath(os.path.join('..','task_data')))
from task_data.trello_helper import TrelloHelper

class SendMessages():
    '''
    Class that reads Trello reminders and uses other helper classes to actually
        send messages
    '''
    def __init__(self):
        '''
        Default constructor
        '''
        self.c = ContactList()
        self.tw = TwilioHelper()
        self.tr = TrelloHelper()
        self.s = SendGridHelper()
        self.f = FBChatHelper()

    def send_all_messages(self, msg_type) -> None:
        '''
        Sends messages to members by reading in all reminders and then for each
            member individually forming message and sending requests
        '''
        members_reminders = self.tr.get_hack_members_reminders()
        # Key: member, Value: [tasks]
        for member, tasks in members_reminders.items():
            msg = "Hello " + member + ",\n\nHere are your Trello tasks:\n\n"
            for task in tasks:
                msg += task + "\n"

            if member in self.c.contacts.keys():
            # Key: User, Value: [email, phone number]
                # SendGrid's email format is plain text so paragraph breaking
                # is somewhat buggy
                if msg_type == "email":
                    self.s.email_user(msg.replace("\n","\n\n"), self.c.contacts[member]["Email"])
                elif msg_type == "text":
                    self.tw.text_user(msg, self.c.contacts[member]["Number"])
                elif msg_type == "fb":
                    self.f.message_user(msg, member)
                    sleep(3)
                else:
                    self.s.email_user(msg.replace("\n","\n\n"), self.c.contacts[member]["Email"])
                    self.tw.text_user(msg, self.c.contacts[member]["Number"])
                    self.f.message_user(msg, member)
                    sleep(3)

    def send_indv_message(self, name, msg_type):
        member_reminders = self.tr.get_hack_specific_member_reminders(name)
        tasks = list(member_reminders.values())[0] #Casts the dict values to lists
        msg = "Hello " + name + ",\n\nHere are your Trello tasks:\n\n"
        for task in tasks:
            msg += task + "\n"

        if name in self.c.contacts.keys():
            if msg_type == "email":
                self.s.email_user(msg.replace("\n","\n\n"), self.c.contacts[name]["Email"])
            elif msg_type == "text":
                print(self.c.contacts[name])
                self.tw.text_user(msg, self.c.contacts[name]["Number"])
            elif msg_type == "fb":
                self.f.message_user(msg, name)
                sleep(3)
            else:
                self.s.email_user(msg.replace("\n","\n\n"), self.c.contacts[name]["Email"])
                self.tw.text_user(msg, self.c.contacts[name]["Number"])
                self.f.message_user(msg, name)
                sleep(3)
