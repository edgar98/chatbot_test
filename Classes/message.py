import datetime

from Classes.settings import EmojiType


class Message:
    """
    This class describes Message object
    """
    def __init__(self, string: str):
        """
        Initialization of Message
        :param string: text of message
        """
        self.text = string
        self.time = datetime.datetime.now()
        self.session_id = None  # session ID is generated later
        self.client_id = None  # client_id isn't used anywhere in this project, so it will be equal session ID later
        self.type = EmojiType.NONE  # set default content emotional type

    def set_session_id(self, session):
        """
        Setter for session ID
        :param session: Session object
        """
        self.session_id = session.get_id()

    def set_type(self, emoji_type):
        """
        Setter for message content emotion type
        :param emoji_type: EmojiType object
        :type emoji_type: Classes.settings.EmojiType
        """
        self.type = emoji_type
