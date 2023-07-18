#author: Alice Heranval
#filename = name of downloaded csv file with list of scans taken from tapas website.

def csvMaker(filename):
    file = open(filename)
    file.readline()
    f = file.readlines()
    file.close()
    n = open("IRAM_Data.csv", "w")
    n.write("ID,Start Time,End Time,Date,Source Name")
    for line in f:
        l = line.split(",")
        id = l[0][11:]
        st = l[2][11:]
        et = l[3][11:]
        date = l[0][:10]
        source = l[4]
        obs_type = l[6]
        if source[0] == "J" and obs_type == "onTheFlyMap":
            n.write(f"\n{id},{st},{et},{date},{source}")
    n.close()
