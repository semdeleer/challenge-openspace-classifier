import csv
from utils.openspace import Openspace
from utils.table import Table

csv_file_path = r"C:\Users\semde\BeCodeH\Projects\Project1\challenge-openspace-classifier/new_colleagues.csv"
names_list = []

with open(csv_file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        name = row[0]
        names_list.append(name)

print(names_list)



