import requests
import urllib.parse
class DhiraaguBulkSMS:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Send message
    def send_message(self, mobile_number, msg):
        if not self.username or not self.password:
            print("Username and password not set")
            quit()

        self.mobile_number = mobile_number

        # Validate mobile number
        if self.validate_number() == False:
            print("Invalid mobile number")
            quit()

        enc_msg = urllib.parse.quote(msg)
        requests.get('https://bulkmessage.dhiraagu.com.mv/jsp/receiveSMS.jsp?userid='+self.username+'&password='+self.password+'&to='+self.mobile_number+'&text='+enc_msg)

    # Validate mobile number
    def validate_number(self):
        # Check if mobile number has 10 digits
        if len(self.mobile_number) != 10:
            return False
        # Check if mobile number prefix starts from 960
        if self.mobile_number[0:3] != '960':
            return False
        # Check if mobile number starts with 7 or 9
        if self.mobile_number[4] != '7' or self.mobile_number[4] != '9':
            return False

        # If all good, return true
        return True