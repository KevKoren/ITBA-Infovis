import csv
import datetime
import json

sourcePath = "barrios.csv"

destPath = "barrios_tableau.csv"

sourceFile = open(sourcePath,"r")
destFile = open(destPath, "w", newline='')

reader = csv.reader(sourceFile)
writer = csv.writer(destFile)

#Escribo el header
current = reader.__next__()
writer.writerow(['BARRIO', 'Latitud', 'Longitud', "País/Región", "Estado/Provincia"])

current = reader.__next__()

try:
    while current:
        writer.writerow([current[0], current[5], current[4], "Argentina", "Ciudad de Buenos Aires"])
        current = reader.__next__()
except StopIteration:
    pass


sourceFile.close()
destFile.close()
