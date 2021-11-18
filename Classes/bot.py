from Classes.FSM_answer_generator import FSMGenerator
from Classes.message import Message
from Classes.message_processor import MessageProcessor
from Classes.session import SessionManager
from Classes.settings import EMOJIS, EMOJIS_TEST
from Classes.db import DataBase


class Bot:
    def __init__(self):
        self.alphabet = EMOJIS
        # self.alphabet = EMOJIS_TEST
        self.db = DataBase()  # database connection
        self.message_processor = MessageProcessor(self.alphabet, FSMGenerator())
        self.session_manager = SessionManager(self.db)

    def start(self) -> None:
        """
        Start bot's running
        """
        running = True
        while running:

            curr_message = Message(input())  # get message from user

            if curr_message.text == 'exit':  # command to exit running properly
                running = False

            if self.session_manager.get_session().get_context():
                time_delta = curr_message.time - \
                             self.session_manager.get_session().get_context().time  # calculate time delta
                if time_delta.total_seconds() > 60:  # if message received after 1 minute from last message
                    self.session_manager.close_current_session()  # close session

            curr_message.set_session_id(self.session_manager.get_session())  # link received message to session
            self.db.save_message(curr_message)  # save message

            answer, error = self.message_processor.process(  # send message processing to MessageProcessor
                curr_message,
                self.session_manager.get_session().get_context()
            )

            print(answer)
            if not error:  # if answer wasn't error
                self.session_manager.get_session().set_context(curr_message)  # save curr_message to context
            else:
                self.session_manager.get_session().set_context(None)  # delete context

        self.session_manager.close_current_session()  # close session on exit
