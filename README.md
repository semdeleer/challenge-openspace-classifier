# challenge-openspace-classifier

## Introduction

This project aims to create an algorithm for efficiently assigning individuals to tables.

## Usage

Import a file containing a list of occupant names and incorporate it into the main.py file. Once the list is provided as input in main.py, the program will automatically generate seating arrangements, assigning individuals to available tables and spaces.

## Classes

### Class Openspace
<ul>
    <li><strong>Attributes:</strong></li>
    <ul>
        <li><code>number_of_tables</code> (int): The total number of tables in the openspace.</li>
        <li><code>tables</code> (list): A list of Table objects representing each table in the openspace.</li>
    </ul>
</ul>

<ul>
    <li><strong>Methods:</strong></li>
    <ul>
        <li><code>__init__(self, number_of_tables, capacity_per_table)</code>: Initializes an Openspace instance.</li>
        <li><code>organize(self, names)</code>: Organizes a list of names into seats at the tables.</li>
        <li><code>display(self)</code>: Displays the current seating arrangement at each table.</li>
        <li><code>store(self, filename)</code>: Stores the current seating arrangement in a file.</li>
    </ul>
</ul>


### Class Table
<ul>
    <li><strong>Attributes:</strong></li>
    <ul>
        <li><code>capacity</code> (int): The maximum number of seats available at the table.</li>
        <li><code>seats</code> (list): A list of Seat objects representing each seat at the table.</li>
    </ul>
</ul>

<ul>
    <li><strong>Methods:</strong></li>
    <ul>
        <li><code>__init__(self, capacity)</code>: Initializes a Table instance.</li>
        <li><code>has_free_spot(self)</code>: Checks if there is at least one unoccupied seat at the table.</li>
        <li><code>assign_seat(self, name)</code>: Assigns a name to the first available unoccupied seat at the table.</li>
        <li><code>left_capacity(self)</code>: Returns the number of unoccupied seats at the table.</li>
    </ul>
</ul>


### Class Seat
<ul>
    <li><strong>Attributes:</strong></li>
    <ul>
        <li><code>name</code> (str): The name of the occupant.</li>
        <li><code>occupant</code> (str): Empty string.</li>
        <li><code>free</code> (bool): A boolean to indicate if a seat is empty.</li>
    </ul>
</ul>

<ul>
    <li><strong>Methods:</strong></li>
    <ul>
        <li><code>__init__(self, name)</code>: Initializes a Seat instance.</li>
        <li><code>set_occupant(self, name)</code>: Changes the <code>free</code> attribute to False and adds the <code>name</code> to the <code>occupant</code>.</li>
        <li><code>remove_occupant(self)</code>: Removes the occupant from a seat and changes the <code>free</code> attribute back to True.</li>
        <li><code>__str__(self)</code>: Returns if the seat is taken and if so, who is in that seat.</li>
    </ul>
</ul>


## Usage
tables_becode = Openspace(6, 4)
tables_becode.organize(names_list)
tables_becode.display()
tables_becode.store(r"C:\Users\semde\BeCodeH\Projects\Project1\challenge-openspace-classifier\utils\tables.txt")