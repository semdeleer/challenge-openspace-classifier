from .table import Table
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
            while current_table < self.number_of_tables and not self.tables[current_table].has_free_spot():
                current_table += 1
            
            if current_table == self.number_of_tables:
                print(f"No avaible seats for {name}")
                break

        result = self.tables[current_table].assign_seat(name)
        print(result)
    
    def display(self):
        for i, table in enumerate(self.tables):
            print(f"Table {i + 1}")
            for seat in table.seats:
                print(f"{seat}")

    def store(self, filename):
        new_tablefile = filename
        file = open(new_tablefile, "w")
        for i, table in enumerate(self.tables):
            file.write(f"Table{i + 1} \n")
            for seat in table.seats:
                file.write(f"Seat {seat}")
        file.close()

