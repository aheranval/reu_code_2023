# Author: Alice Heranval
# filename: name of csv file with data in format given by csvMaker.py
# band: band of observations (1, 2, 13)

def makeLine(filename, band):
    sourceList = ['J1641', 'J1509', 'J1228', 'J1510', 'J1522']
    source = input(f"which source? ({str(sourceList)}) ")
    mystr = "ls "
    f = open(filename)
    f.readline()
    file = f.readlines()
    f.close()
    count = 0
    for l in file:
        line = l.strip().split(",")
        date = line[3].split("-")
        if line[-1] == source:
            count += 1
            if band != 13:
                mystr += f"*-{band}-*{date[0]}{date[1]}{date[2]}s{line[0]}* "
            else:
                mystr += f"*-1-*{date[0]}{date[1]}{date[2]}s{line[0]}* *-3-*{date[0]}{date[1]}{date[2]}s{line[0]}* "
    mystr += f"> ~/test/{source}_ar{band}.LIST"
    print(mystr)
    print(f"Counted {count} instances of source {source}")


    
