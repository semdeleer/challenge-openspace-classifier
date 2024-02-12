class Seat:
    """
     Seat class: Gives back if the seat on the table is occupied or not
     param: The name of the occupant of the seat

     set_occupant: sets the occupant on an empty seat
     remove_occupant: removes the occupant from a seat
    """

    def __init__(self, name) -> None:
        self.free = True
        self.occupant = ""
        self.name = name

    def set_occupant(self, name):
        if self.free:
            self.free = False
            self.occupant = name

    def remove_occupant(self):
        self.free = True
        return f"The occupant was {self.occupant}"

    def __str__(self) -> str:
        return f"The seat is {self.free} and if it's not free, the occupant is {self.occupant}"


class Table:
    """
    Table class represents a table with a specific seating capacity and seats.

    Attributes:
    - capacity (int): The maximum number of seats available at the table.
    - seats (list): A list of Seat objects representing each seat at the table.

    Methods:
    - __init__(self, capacity): Initializes a Table instance with the specified seating capacity.
    - has_free_spot(self): Checks if there is at least one unoccupied seat at the table.
    - assign_seat(self, name): Assigns a name to the first available unoccupied seat at the table.
    - left_capacity(self): Returns the number of unoccupied seats at the table.

    """

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.seats = [Seat(f"Seat {i+1}") for i in range(self.capacity)]

    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return f"{name} assigned to {seat.name}"
        return f"No available seats for {name}"

    def left_capacity(self):
        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
        return count

# Create a Table with an initial capacity of 4
#table = Table(4)

# Assign John to the table
#result = table.assign_seat("John")
#result1 = table.assign_seat("Mary")
#print(result)
#print(result1)

# Check the left capacity of the table
#left_capacity = table.left_capacity()
#print(f"Table has {left_capacity} free seats.")
