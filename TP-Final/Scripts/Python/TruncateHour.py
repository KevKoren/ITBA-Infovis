import csv
import datetime

sourcePath = "log_con_barrios.csv"

destPath = "log_con_barrios_hora_truncada.csv"

sourceFile = open(sourcePath,"r")
destFile = open(destPath, "w", newline='')

reader = csv.reader(sourceFile)
writer = csv.writer(destFile)

#Escribo el header
current = reader.__next__()
writer.writerow(current)

current = reader.__next__()
try:
    while current:
        #Trunco minutos y segundos
        current[1] = datetime.datetime.strptime(current[1], "%Y-%m-%d %H:%M:%S").replace(minute = 0, second=0).strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow(current)
        current = reader.__next__()
except StopIteration:
    pass

sourceFile.close()
destFile.close()
