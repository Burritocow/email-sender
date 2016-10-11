from config.Properties import Properties

class Email:
    def __init__(self, dict):
        self.subject = dict["subject"]
        self.from_address = dict["fromAddress"]
        self.reply_to_address = dict["replyToAddress"]

class Student:
    def __init__(self, last_name, first_name, email_address):
        self.last_name = last_name
        self.first_name = first_name
        self.email_address = email_address
