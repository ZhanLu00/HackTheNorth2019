import utils
import backend
from threading import Thread, Event

user_info = []

start_analysis = Event()
start_analysis.clear()

def _conversation():
    with open("conversation.txt", 'r') as file:

        for _ in range(3):
            utils.speak(file.readline())
        
        user_info.append(input("Please enter your name: "))
        user_info.append(input("Please enter your home address: "))

        for _ in range(2):
            utils.speak(file.readline())

        user_info.append(utils.get_expenditure())

        start_analysis.set()

        for _ in range(9):
            utils.speak(file.readline())

        for _ in range(2):
            utils.speak(file.readline())

conversation_thread = Thread(name="Conversation", target=_conversation)
analysis_thread = Thread(name="Analysis", target=backend.analysis)
analysis_thread.setDaemon(False)

def run():
    conversation_thread.start()
    start_analysis.wait()
    analysis_thread.start()
    analysis_thread.join()

run()