# Author: Alice Heranval
# filename: name of csv file with data in format given by csvMaker.py
# band: band of observations (1, 2, 13)
# directory: the directory where you are conducting data reduction
# copy paste printed line (mystr) into command line
# must be within directory containing data to work (ex: cd imbfitsDir)
# input statement is to help with remembering which source is needed. Otherwise can simply change source to be a parameter.

def makeLine(filename, band, directory):
    sourceList = ['J1641', 'J1509', 'J1228', 'J1510', 'J1522'] # assuming only these sources are observed
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
    mystr += f"> ~/{directory}/{source}_ar{band}.LIST"
    print(mystr) # or return if you prefer
    #print(f"Counted {count} instances of source {source}") ## only if needed to count files used or observations of source made


    
