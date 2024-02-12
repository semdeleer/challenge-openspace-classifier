# challenge-openspace-classifier

## Introduction

This project aims to create an algorithm for efficiently assigning individuals to tables.

## Usage

Import a file containing a list of occupant names and incorporate it into the main.py file. Once the list is provided as input in main.py, the program will automatically generate seating arrangements, assigning individuals to available tables and spaces.

## Classes

### Openspace Class
- Attributes
-- number_of_tables (int): The total number of tables in the openspace.
-- tables (list): A list of Table objects representing each table in the openspace.

-Methods
-- __init__(self, number_of_tables, capacity_per_table): Initializes an Openspace instance.
-- organize(self, names): Organizes a list of names into seats at the tables.
-- display(self): Displays the current seating arrangement at each table.
-- store(self, filename): Stores the current seating arrangement in a file.

### Class Table
- Attributes
-- capacity (int): The maximum number of seats available at the table.
-- seats (list): A list of Seat objects representing each seat at the table.

-Methods
-- __init__(self, capacity): Initializes a Table instance.
-- has_free_spot(self): Checks if there is at least one unoccupied seat at the table.
-- assign_seat(self, name): Assigns a name to the first available unoccupied seat at the table.
-- left_capacity(self): Returns the number of unoccupied seats at the table.

### Class Seat
- Attributes
-- name  (str): The name of the occupant
-- occupant (str): empty string
-- free (bool): A boolean to see of a seat is empty

-Methods
-- __init__(self, name): Initializes a Table instance.
-- set_occupant(self, name): changes the free to False and add the name to the occupant
-- remove_occupant(self): Removes the occupeant from a seat and changes the free attribute back to True
-- __str__(self): return if the seat is taken and if so who is in that seat

## Usage
tables_becode = Openspace(6, 4)
tables_becode.organize(names_list)
tables_becode.display()
tables_becode.store(r"C:\Users\semde\BeCodeH\Projects\Project1\challenge-openspace-classifier\utils\tables.txt")