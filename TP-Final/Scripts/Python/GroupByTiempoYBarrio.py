import csv
import logging
import time

def separarYEscribirBarrios(groupTiempo, writer):
    # Con la lista de cierta hora genero un diccionario con sus barrios y la cantidad de busquedas para esa hora
    groupBarrio = {}
    for row in groupTiempo:
        if not row[4] in groupBarrio:
            groupBarrio[row[4]] = 1
        else:
            groupBarrio[row[4]] += 1
    # Escribo
    for (k, v) in groupBarrio.items():
        writer.writerow([current[1], k, v])


sourcePath = "log_con_barrios_hora_truncada.csv"

destPath = "log_con_barrios_agrupados.csv"

sourceFile = open(sourcePath,"r")
destFile = open(destPath, "w", newline='')

reader = csv.reader(sourceFile)
writer = csv.writer(destFile)

#Salteo y escribo el nuevo header
current = reader.__next__()
writer.writerow(["fechahora", "barrio", "cantidad_busquedas"])

current = reader.__next__()
next = []

groupTiempo = []
groupBarrio = {}

startTime = time.time()
lastTime = startTime
try:
    while current:
        groupTiempo.append(current)
        next = reader.__next__()
        # Mientras sea la misma hora agrego el registro a la lista
        while next[1] == current[1]:
            groupTiempo.append(next)
            next = reader.__next__()

        separarYEscribirBarrios(groupTiempo, writer)

        #logs en stdout
        print("Última Hora escrita: " + str(current[1]))
        print("Tiempo en procesar hora: %d segundos." % (time.time() - lastTime))
        lastTime = time.time()
        groupTiempo = []
        current = next
except StopIteration:
    # Manejo la última hora
    separarYEscribirBarrios(groupTiempo, writer)
    groupTiempo = []

    #logs en stdout
    print("Última Hora escrita: " + str(current[1]))
    print("Tiempo en procesar hora: %d segundos." % (time.time() - lastTime))

#logs en stdout
print("Fin de Horas.")
print("Tiempo total: %d segundos" % (time.time() - startTime))

sourceFile.close()
destFile.close()
