import requests
import urllib.parse
class DhiraaguBulkSMS:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Send message
    def send_message(self, mobile_number, msg):
        if not self.username or not self.password:
            return "Username and password not set"

        self.mobile_number = '960' + mobile_number

        # Validate mobile number
        if self.validate_number() == False:
            return "Invalid mobile number"

        enc_msg = urllib.parse.quote(msg)
        response = requests.get('https://bulkmessage.dhiraagu.com.mv/jsp/receiveSMS.jsp?userid=' + self.username + '&password=' + self.password + '&to=' + self.mobile_number + '&text=' + enc_msg)

        return response.content.decode('utf-8')

    # Validate mobile number
    def validate_number(self):

        # Check if mobile number has 10 digits
        if len(self.mobile_number) != 10:
            return False

        # Check if mobile number starts with 7 or 9
        if self.mobile_number[4] != '7' and self.mobile_number[4] != '9':
            return False

        # If all good, return true
        return True