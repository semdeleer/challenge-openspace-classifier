class Seat:
    """
     Seat class: Gives back if the seat on the table is occupatied or not
    """

    def __init__(self, name) -> None:
        self.free = False
        self.occupant = ""
        self.name = name

    def set_occupant(self, name):
        if self.free == False:
            self.free = True
            self.occupant = name

    def remove_occupant(self):
        self.free = False
        return f"The occupant was{self.occupant}"

    def __str__(self) -> str:
        return f"The seat is {self.free} and if its not free the occupant is {self.name}"
    

class Table:
    """
    Table class:
    """

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = [None] * self.capacity

    def has_free_spot(self):
        for i in self.size:
            if i == None:
                return True
            return False

    def assign_seat(self, name):
        if self.has_free_spot(self) == True:
            for i in self.size:
                if i == None:
                    self.size[i] = name
    
    def left_capacity(self):
        count = 0
        for i in self.size:
            if i == None:
                count += 1
        return count


        