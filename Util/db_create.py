import sqlite3

try:
    sqlite_connection = sqlite3.connect('../emoji_bot.db')
    cursor = sqlite_connection.cursor()

    create_message_table = '''CREATE TABLE messages (
                                id INTEGER PRIMARY KEY, 
                                msg_time TIMESTAMP NOT NULL, 
                                session_id INTEGER NOT NULL, 
                                msg_text TEXT NOT NULL, 
                                client_id INTEGER NOT NULL, 
                                FOREIGN KEY (session_id) REFERENCES sessions(id)
                            );'''

    create_session_table = '''CREATE TABLE sessions (
                                id INTEGER PRIMARY KEY, 
                                start_time TIMESTAMP NOT NULL, 
                                stop_time TIMESTAMP
                            );'''

    cursor.execute(create_session_table)
    cursor.execute(create_message_table)
    cursor.close()

except sqlite3.Error as error:
    print(error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
