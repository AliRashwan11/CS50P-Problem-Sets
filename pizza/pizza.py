import sys
from tabulate import tabulate
import csv

lines=[]

if not len(sys.argv) == 2:
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
    else:
        print("Too few command-line arguments")
    sys.exit()
else:
    filename=sys.argv[1]
    if not "." in filename:
        print("Not a CSV file ")
        sys.exit()
    splt=filename.split(".")
    extension=splt[1]
    if not extension=="csv":
        print("Not a CSV file")
        sys.exit()
    else:
        try:
            file=open(filename)
        except FileNotFoundError:
            print("File does not exist")
            sys.exit()

        rdr=csv.reader(file)
        for line in rdr:
            lines.append(line)
        print(tabulate(lines[1:],headers=lines[0],tablefmt="grid"))

       
