import datetime

from Classes.db import DataBase
from Classes.message import Message


class Session:
    """
    Describes session
    """
    def __init__(self, _id: int, start_time: datetime.datetime):
        self._id = _id
        self.start_time = start_time
        self.stop_time = None
        self.context = None

    def stop(self) -> None:
        """
        Closes session by setting stop time
        """
        self.stop_time = datetime.datetime.now()

    def get_id(self) -> int:
        """
        Getter for ID
        :return: ID
        """
        return self._id

    def get_stop_time(self) -> datetime.datetime:
        """
        Getter for stop time
        :return: Stop_time
        """
        return self.stop_time

    def set_context(self, context: Message) -> None:
        """
        Setter for context
        :param context: Message for save as context
        """
        self.context = context

    def get_context(self) -> Message:
        """
        Getter for context
        :return: Context Message
        """
        return self.context


class SessionManager:
    """
    This class describes sessions' logic
    """
    def __init__(self, db: DataBase):
        self._curr_session = None
        self._db = db

    def get_session(self) -> Session:
        """
        Returns session if exist or returns new one
        :return: Session
        """
        if not self._curr_session:  # if no session exist
            self._create_session()  # create session
        return self._curr_session  # return Session

    def close_current_session(self) -> None:
        """
        Closes current stored session
        """
        if self._curr_session:
            self._curr_session.stop()
            self._db.close_session(self._curr_session)
            self._curr_session = None

    def _create_session(self) -> None:
        """
        Creates new Session
        """
        curr_time = datetime.datetime.now()
        session_id = self._db.create_session(curr_time)
        self._curr_session = Session(session_id, curr_time)
