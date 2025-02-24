# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    #method parse
    def parse(self):
        #finds emails with spaces, commas
        email_list = re.split(r'[,\s]+', self.email_addresses.strip())

        #email validation as of previous test
        email_pattern = r"^[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        #filter valid emails
        valid_emails = sorted(set(email for email in email_list if re.match(email_pattern, email)))

        #removes any accidental empty string
        return valid_emails