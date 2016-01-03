"""Exploring data in a manageable way"""

import csv

sourcePath = "log_dirs_mapa_latlong.csv"

file = open(sourcePath,"r")

reader = csv.reader(file)

current = reader.__next__()

setXY = {}

try:
    while current:
        try:
            setXY[str(current[1]) + str(current[2])] += 1
        except Exception:
            setXY[str(current[1]) + str(current[2])] = 1
        current = reader.__next__()
except StopIteration:
    pass

file.close()

repetitives1 = 0
repetitives5 = 0
repetitives10 = 0
repetitives20 = 0
repetitives50 = 0
repetitives100 = 0
repetitivesMore100 = 0

for i in setXY:
    if setXY[i] == 1:
        repetitives1 += 1
    elif setXY[i] <= 5:
        repetitives5 += 1
    elif setXY[i] <= 10:
        repetitives10 += 1
    elif setXY[i] <= 20:
        repetitives20 += 1
    elif setXY[i] <= 50:
        repetitives50 += 1
    elif setXY[i] <= 100:
        repetitives100 += 1
    else:
        repetitivesMore100 += 1

print("Different locations: %d\n" % len(setXY))
print("Locations with 1 search: %d" % repetitives1)
print("Locations with more than 1 and less than 6 searchs: %d" % repetitives5)
print("Locations with more than 5 and less than 10 searchs: %d" % repetitives10)
print("Locations with more than 10 and less than 21 searchs: %d" % repetitives20)
print("Locations with more than 20 and less than 51 searchs: %d" % repetitives50)
print("Locations with more than 50 and less than 101 searchs: %d" % repetitives100)
print("Locations with more than 100 searchs: %d" % repetitivesMore100)
