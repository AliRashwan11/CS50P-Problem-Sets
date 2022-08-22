import sys
import csv

names=[]
firstnames=[]
lastnames=[]
places=[]
finlist=[]

if not len(sys.argv)==3:
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")
else:
    beforefile=sys.argv[1]
    afterfile=sys.argv[2]
    if not "." in beforefile:
        sys.exit("Could not read " + beforefile)
    if not "." in afterfile:
        sys.exit("Could not write to " + afterfile)
    try:
        file1=open(beforefile)
    except FileNotFoundError:
        sys.exit("Could not read " + beforefile)
    
    rdr=csv.reader(file1)
    for line in rdr:
        if line==['name','house']:
            continue
        else:
            name=line[0]
            place=line[1]
            names.append(name)
            places.append(place)

    for line in names:
        splt=line.split(",")
        first=splt[1].lstrip()
        second=splt[0].lstrip()
        firstnames.append(first)
        lastnames.append(second)

    for i in range(len(firstnames)):
        newlist=[]
        newlist.append(firstnames[i])
        newlist.append(lastnames[i])
        newlist.append(places[i])
        finlist.append(newlist)

    file2=open(afterfile,"w",newline="")
    wrtr=csv.writer(file2)

    frstline=["first","last","house"]
    wrtr.writerow(frstline)

    for line in finlist:
        wrtr.writerow(line)
