import pyrebase
from time import sleep
from random import randrange

firebaseConfig = {
    "apiKey": "AIzaSyBRebJ4woEHzvPM0NeG2f49c7-atJQkdmM",
    "authDomain": "sample-f4a88.firebaseapp.com",
    "databaseURL": "https://sample-f4a88.firebaseio.com",
    "projectId": "sample-f4a88",
    "storageBucket": "sample-f4a88.appspot.com",
    "messagingSenderId": "535786291215",
    "appId": "1:535786291215:web:7fed87cb6d845a718f237a"
}

firebase = pyrebase.initialize_app(firebaseConfig)

class Analysis:

    def __init__(self):
        self.auth = firebase.auth()
        self.user = None
        
    def authentication(self):        
        option = input("Sign up/ Login in <1/2>: ")

        if option == '1':
            while not self.user:
                email = input("Email: ")
                password = input("Password: ")
                self.user = self.auth.create_user_with_email_and_password(email, password)
        else:            
            while not self.user:
                email = input("Email: ")
                password = input("Password: ")

                self.user = self.auth.sign_in_with_email_and_password(email, password)
            else:
                return True


        # auth.send_email_verification(user['idToken'])
        # auth.send_password_reset_email(user['idToken'])

        # auth.get_account_info(user['idToken'])

def get_expenditure():
    expenditure = None

    while not expenditure:
        try:
            expenditure = float(input(""))
        except Exception:
            print("Please be a number!")
    
    return expenditure
    
def speak(text):
    print(text)
    sleep(randrange(0, 2))

