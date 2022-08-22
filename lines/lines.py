import sys

LOC=0

if len(sys.argv)==0:
    sys.exit()

if not len(sys.argv) == 2:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

else:
    filename=sys.argv[1]
    if not "." in filename:
        sys.exit("Not a python file")
    else:
        splt=filename.split(".")
        extension=splt[1]
        if not extension == "py":
            sys.exit("Not a python file")
        else:
            try:
                file=open(filename)
            except FileNotFoundError:
                sys.exit("File does not exist")
            lines=file.readlines()
            for line in lines:
                line=line.lstrip()
                if line.strip()=="" or line[0]=="#":
                    continue
                else:
                    LOC=LOC+1
            print(LOC)