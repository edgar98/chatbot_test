import datetime


class Session:
    """
    Describes session
    """
    def __init__(self, _id: int, start_time: datetime.datetime):
        self._id = _id
        self.start_time = start_time
        self.stop_time = None
        self.context = None

    def stop(self):
        """
        Closes session by setting stop time
        """
        self.stop_time = datetime.datetime.now()

    def get_id(self):
        """
        Getter for ID
        :return: ID
        """
        return self._id

    def get_stop_time(self):
        """
        Getter for stop time
        :return: Stop_time
        """
        return self.stop_time

    def set_context(self, context):
        """
        Setter for context
        :param context: Message for save as context
        """
        self.context = context

    def get_context(self):
        """
        Getter for context
        :return: Context Message
        """
        return self.context


class SessionManager:
    """
    This class describes sessions' logic
    """
    def __init__(self, db):
        self._curr_session = None
        self._db = db

    def get_session(self):
        """
        Returns session if exist or returns new one
        :return: Session
        """
        if not self._curr_session:  # if no session exist
            self._create_session()  # create session
        return self._curr_session  # return Session

    def close_current_session(self):
        """
        Closes current stored session
        """
        if self._curr_session:
            self._curr_session.stop()
            self._db.close_session(self._curr_session)
            self._curr_session = None

    def _create_session(self):
        """
        Creates new Session
        """
        curr_time = datetime.datetime.now()
        session_id = self._db.create_session(curr_time)
        self._curr_session = Session(session_id, curr_time)
