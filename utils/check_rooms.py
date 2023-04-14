from conn_db import Connection


class CheckAvailabilityRoom(Connection):

    def check_availability(self):
        print('verificando disponibilidade')
        query = "SELECT * FROM rooms WHERE disponivel = 'S'"
        self.cursor.execute(query)
        avaiable_rooms = self.cursor.fetchall()

        if avaiable_rooms:
            output = ""
            for room in avaiable_rooms:
                output += f"room {room[0]}: Available (not reserved).\n"
            return output
        else:
            query = "SELECT * FROM rooms ORDER BY check_out ASC LIMIT 1"
            self.cursor.execute(query)
            first_unoccupied_room = self.cursor.fetchone()
            if first_unoccupied_room:
                return f"No room available. O room {first_unoccupied_room[0]} will be vacated first in {first_unoccupied_room[2]}"
            else:
                return "No room available and there is no close check out date"


verify = CheckAvailabilityRoom()
result = verify.check_availability()
print(result)
