import csv
from utils.openspace import Openspace


csv_file_path = r"C:\Users\semde\BeCodeH\Projects\Project1\challenge-openspace-classifier/lesColl.csv"
names_list = []

with open(csv_file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        name = row[0]
        names_list.append(name)





tables_becode = Openspace(6, 4)
tables_becode.organize(names_list)
tables_becode.display()
tables_becode.store(r"C:\Users\semde\BeCodeH\Projects\Project1\challenge-openspace-classifier\utils\tables.txt")