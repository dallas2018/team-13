import trello
import json

class TrelloHelper():
    '''
    Class that extracts data from the Trello API using Py-Trello and creates reminder messages for each user
    '''

    def __init__(self):
        '''
        Default constructor
        '''

        # Todo: put all of the key, secret, and tokens to env variables when deploying
        try:
            #Loads credentials from the credential file
            with open("credentials.json") as f:
                creds = json.load(f)

            self.client = trello.TrelloClient(
                api_key=creds["trello"]["api_key"],
                api_secret=creds["trello"]["api_secret"],
                token=creds["trello"]["token"]
            )
        except:
            raise TrelloAuthException

        all_boards = self.client.list_boards()
        self.hack_board = all_boards[2]  # Second index is the hack board
        self.hack_members = self.hack_board.get_members()

    def get_hack_specific_member_reminders(self,name):
        '''
        Method that gets the tasks for a specific hack member
        :param: name: String. Name of the person who needs to be reminded
        :return: hack_reminders: Dictionary. Key are the hack members. Values are the formatted task reminders.
        '''

        #Dictionary of members and their reminders
        hack_reminders = {}

        #Refreshes the cache every single time we perform a reminder
        checklist_cache = self._populate_checklist_cache()

        # Loops through members and gets all of their associated tasks and due dates
        for member in self.hack_members:

            reminder_list = []

            # Check to find the specific member you are looking for
            if member.full_name == name:

                for card in member.fetch_cards():
                    # Name, Due Date, Checklist, non checked items
                    card_id = card["id"]
                    card_name = card["name"]
                    card_due = card["due"]
                    card_desc = card["desc"]

                    # Checks if the checklist exists
                    if card_id in checklist_cache:
                        card_checklist = checklist_cache[card_id]
                        card_tasks = self._get_checklist_tasks(card_checklist)

                    else:
                        card_tasks = "No Tasks"

                    reminder_string = self._format_reminder_string(card_name, card_due, card_tasks)
                    reminder_list.append(reminder_string)

                hack_reminders[member.full_name] = reminder_list

                return hack_reminders

        return hack_reminders

    def get_hack_members_reminders(self):
        '''
        Method that gets all reminders for hack members and returns them in dictionary format
        :return: hack_reminders: Dictionary. Key are the hack members. Values are the formatted task reminders.
        '''

        #Dictionary of members and their reminders
        hack_reminders = {}

        #Refreshes the cache every single time we perform a reminder
        checklist_cache = self._populate_checklist_cache()

        # Loops through members and gets all of their associated tasks and due dates
        for member in self.hack_members:

            reminder_list = []

            # Skip Ryan since he manages tasks
            if member.full_name == "Ryan Luu":
                continue

            for card in member.fetch_cards():
                # Name, Due Date, Checklist, non checked items
                card_id = card["id"]
                card_name = card["name"]
                card_due = card["due"]
                card_desc = card["desc"]

                #Checks if the checklist exists
                if card_id in checklist_cache:
                    card_checklist = checklist_cache[card_id]
                    card_tasks = self._get_checklist_tasks(card_checklist)

                else:
                    card_tasks = "No Tasks"

                reminder_string = self._format_reminder_string(card_name, card_due, card_tasks)
                reminder_list.append(reminder_string)

            hack_reminders[member.full_name] = reminder_list

        return hack_reminders

    ''' Utility functions for pre-processing data'''
    def _get_hack_board(self,all_boards):
        '''
        Method that looks through each board to find the Hack Marketing Board
        :param all_boards: List. List of boards
        :return: board: Board. Hack Marketing Board
        '''
        for board in self.client.list_boards():
            if board.name == "Hack Marketing Committee":
                return board

    def _populate_checklist_cache(self):
        '''
        Method that pre-populates a dictionary with checklist data to reduce network requests to Trello API
        :return: checklist_cache
        '''

        checklist_cache = {}

        for checklist in self.hack_board.get_checklists():
            checklist_cache[checklist.trello_card] = checklist.items

        return checklist_cache

    def _get_checklist_tasks(self,card_checklist):
        '''
        Method that parses the checklist data into a string of tasks separated by line breaks
        :param card_checklist: List of Dictionaries. Dictionaries contain all information about each checklist entry
        :return: checklist_string: String. String of tasks separated by line breaks
        '''

        checklist_string = ""

        for i in card_checklist:
            checklist_string += i["name"] + "\n"

        return checklist_string

    def _format_reminder_string(self,name, due_date, tasks):
        '''
        Method that formats the trello card information into a reminder string that will be sent to users
        :param name: String. Name of the card
        :param due_date: String. Due date of the card
        :param tasks: String. Tasks in the checklist for the card
        :return: formatted_reminder: String. Clean reminder string
        '''

        formatted_reminder = "Name: {}\nDue Date: {}\nTasks:\n{}".format(name, due_date, tasks)
        return formatted_reminder

''' Exceptions related to the TrelloHelper class'''
class TrelloAuthException(Exception):
    pass

if __name__ == "__main__":
    th = TrelloHelper()
    members_reminders = th.get_hack_members_reminders()

    #Example usage of how to send messages
    for member, tasks in members_reminders.items():

        for task in tasks:
            print(member,task,sep="\n") #TODO: Put messaging code here. Split up and put into a diff class. Just an example

    print("\n",th.get_hack_specific_member_reminders(""))