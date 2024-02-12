from utils.table import Table
class Openspace:
    """
    Class Openspace:
    """

    def __init__(self, number_of_tables, capacity_per_table) -> None:
       self.number_of_tables = number_of_tables
       self.tables = [Table(capacity_per_table) for _ in range(number_of_tables)]

    def organize(self, names):
        current_table = 0
        for name in names:
            while not self.tables[current_table].has_free_spot():
                current_table = (current_table + 1) % self.number_of_tables  # Wrap around
            self.tables[current_table].assign_seat(name)
            current_table = (current_table + 1) % self.number_of_tables  # Move to the next table

    def display(self):
        for i, table in enumerate(self.tables):
            print(f"Table {i + 1}")
            for seat in table.seats:
                if not seat.free:
                    print(f"Seat {seat.name} - Occupant: {seat.occupant}")
                else:
                    print(f"Seat {seat.name} - Unoccupied")

    def store(self, filename):
        new_tablefile = filename
        file = open(new_tablefile, "w")
        for i, table in enumerate(self.tables):
            file.write(f"Table{i + 1} \n")
            for seat in table.seats:
                if not seat.free:
                    file.write(f"Seat {seat.name} - Occupant: {seat.occupant} \n")
                else:
                    file.write(f"Seat {seat.name} - Unoccupied\n")
        file.close()


#name_list = ["Jhon", "Mandel", "Rick", "Dany"]

#tables = Openspace(2, 2)
#tables.organize(name_list)
#tables.display()


