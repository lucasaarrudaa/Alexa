from conn_db import Connection
import datetime
import threading


class Clean(Connection):

    def __init__(self):
        super().__init__()
        self.connection = self.conn
        self.lock = threading.Lock()

    def check_clean(self, id_room):
        '''
        check if the room is already Clean.
        '''
        query = f"SELECT cleaning, date_entry FROM rooms WHERE id_rooms = {id_room}"
        self.cursor.execute(query)
        room = self.cursor.fetchone()

        if not room:
            return "room not found."

        Clean = room[0]
        check_in = room[1]

        if Clean == 'S':
            return "room is already clean."

        cleaning_start_date = datetime.datetime.now()

        # Start cleaning in a separate thread
        t = threading.Thread(target=self.start_clean, args=(
            id_room, check_in, cleaning_start_date))
        t.start()

        return "Clean started in a separate thread."

    def start_clean(self, id_room, check_in, cleaning_start_date):
        '''
        Start cleaning in a separate thread and calculate final Clean date (30 minutes after input date)
        '''
        with self.lock:
            print("starting to clean")
            query = f"UPDATE rooms SET Clean = 'S', cleaning_start_date = '{cleaning_start_date}' WHERE id_rooms = {id_room}"
            self.cursor.execute(query)
            self.conn.commit()

        cleaning_end_date = check_in + datetime.timedelta(minutes=30)

        while datetime.datetime.now() < cleaning_end_date:
            pass

        with self.lock:

            end_cleaning = datetime.datetime.now()

            query = f"UPDATE rooms SET Clean = 'S', check_out = '{cleaning_end_date}', end_cleaning = '{end_cleaning}' WHERE id_rooms = {id_room}"
            self.cursor.execute(query)
            self.conn.commit()

            print(f"Clean completed for the room {id_room}.")


clean_room = Clean()
# ID of the room to be Clean, informed by the user
id_room = int(input("Enter the ID of the room to be Clean:"))
result = clean_room.check_clean(id_room)
print(result)
