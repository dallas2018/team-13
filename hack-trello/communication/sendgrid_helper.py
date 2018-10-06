from json import load
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *


class SendGridHelper():
    '''
    Class that sends reminders to users via email using SendGrid API
    '''
    def __init__(self):
        '''
        Default constructor
        '''
        with open("credentials.json") as f:
            creds = load(f)
        self.api_key = creds["sendgrid"]["api_key"]
        self.sg = SendGridAPIClient(apikey=self.api_key)
        self.emF = creds["sendgrid"]["email"] # Email that texts are sent from

    def email_user(self, message: str, email: str) -> None:
        '''
        Emails user by taking in Trello to-do list and email to send to
        '''
        from_ = Email(self.emF)
        to_ = Email(email)
        subject = "Trello Tasks Update"
        content = Content("text/plain", message)
        mail = Mail(from_, subject, to_, content)
        response = self.sg.client.mail.send.post(request_body=mail.get())
