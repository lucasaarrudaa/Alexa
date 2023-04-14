import mysql.connector


class Connection:

    def __init__(self):
        print("connecting to databse")
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='168843',
            database='alexa'
        )
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
