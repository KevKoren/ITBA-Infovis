"""Exploring data in a manageable way"""

import csv, urllib.request, json, time

sourcePath = "log_dirs_mapa_latlong.csv"

addressesPath = "log_dirs_mapa_latlong_addresses.csv"

file = open(sourcePath,"r")
addressesPathFile = open(addressesPath,"w",  newline='')

writer = csv.writer(addressesPathFile)
reader = csv.reader(file)

current = reader.__next__()

setXY = {}

try:
    while current:
        try:
            setXY[str(current[1]) + "|" + str(current[2])] += 1
        except Exception:
            setXY[str(current[1]) + "|" + str(current[2])] = 1
        current = reader.__next__()
except StopIteration:
    pass

iterated = 0
iParsed = 0
x = 0
start = time.time()
print("Time %s seconds." % str(time.time() - start))
try:
    for i in setXY.keys():
        splitted = i.split("|")
        url = "http://nominatim.openstreetmap.org/reverse?lon=" + splitted[0] + "&lat=" + splitted[1] + "&format=json&zoom=18"
        response = urllib.request.urlopen(url)
        data = response.read()
        print("Last response at: %s seconds" % str(time.time() - start))
        splitted.append(data.decode())
        writer.writerow(splitted)
        time.sleep(1)
        iParsed += 1
        if iParsed % 1000 == 0:
            print("Parsed %d" % iParsed)
            print("Time %s seconds." % str(time.time() - start))
            print(data)
        iterated += 1
        if iterated % 1000 == 0:
            print("Iteratd %d" % iterated)
            print("Time %s seconds." % str(time.time() - start))
except Exception as e:
    print(data)
    raise(e)


addressesPathFile.close()
file.close()
