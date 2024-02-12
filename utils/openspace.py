from random import shuffle
from utils.table import Table
class Openspace:
    """
    Class Openspace represents an open space with multiple tables where individuals can be organized into seats.

    Attributes:
    - number_of_tables (int): The total number of tables in the openspace.
    - tables (list): A list of Table objects representing each table in the openspace.

    Methods:
    - __init__(self, number_of_tables, capacity_per_table): Initializes an Openspace instance with the given number of tables
      and the specified capacity per table.
    - organize(self, names): Organizes a list of names into seats at the tables, considering the capacity of each table.
    - display(self): Displays the current seating arrangement at each table, showing occupied and unoccupied seats.
    - store(self, filename): Stores the current seating arrangement in a file with the specified filename.

    """

    def __init__(self, number_of_tables, capacity_per_table) -> None:
       self.number_of_tables = number_of_tables
       self.tables = [Table(capacity_per_table) for _ in range(number_of_tables)]

    def organize(self, names):
        shuffle(names)
        unassigned_names = []
        current_table = 0
        for name in names:
            while not self.tables[current_table].has_free_spot():
                current_table += 1
                if current_table == self.number_of_tables:
                    unassigned_names.append(name)
                    break
            else:
                self.tables[current_table].assign_seat(name)

            current_table += 1
            if current_table == self.number_of_tables:
                current_table = 0

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


