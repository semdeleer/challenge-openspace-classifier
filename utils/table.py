class Seat:
    """
     Seat class: Gives back if the seat on the table is occupied or not
     param: The name of the occupand of the seat

     set_occupant: sets the occupont on a empty seat
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
    Table class:
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
table = Table(4)

# Assign John to the table
result = table.assign_seat("John")
print(result)

# Check the left capacity of the table
left_capacity = table.left_capacity()
print(f"Table has {left_capacity} free seats.")
