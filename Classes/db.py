import datetime
import sqlite3
import settings
from Classes.message import Message
from Classes.session import Session


class DataBase:
    """
    Class for operations with DataBase
    """
    def __init__(self):
        """
        Object initialization
        """
        try:
            self.con = sqlite3.connect(settings.DB_NAME)  # open connection
            self.cursor = self.con.cursor()  # get cursor
        except sqlite3.Error as error:
            print(error)

    def save_message(self, message: Message) -> None:
        """
        Saves message in DB
        :param message: Message class object
        """
        sql_insert_message = 'INSERT INTO messages(msg_time, session_id, msg_text, client_id) values (?, ?, ?, ?);'
        self.cursor.execute(sql_insert_message, (message.time, message.session_id, message.text, message.session_id))
        self.con.commit()

    def close_session(self, session: Session) -> None:
        """
        Updates session stop time
        :param session: Session object
        """
        sql_alter_session = 'UPDATE sessions SET stop_time = ? WHERE id = ?;'
        data = (session.get_stop_time(), session.get_id())
        self.cursor.execute(sql_alter_session, data)
        self.con.commit()

    def create_session(self, curr_time: datetime.datetime) -> int:
        """
        Creates session row in DB and returns it's ID
        :param curr_time: New session start time
        :return: Session ID
        """
        sql_insert_session = 'INSERT INTO sessions(start_time) VALUES (?);'
        sql_get_last_session = 'SELECT last_insert_rowid();'
        self.cursor.execute(sql_insert_session, (curr_time,))
        self.cursor.execute(sql_get_last_session)
        self.con.commit()
        records = self.cursor.fetchall()
        for row in records:
            return row[0]

    def exit(self) -> None:
        """
        Close DB connection
        """
        self.cursor.close()
        self.con.close()
