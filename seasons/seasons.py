from datetime import date
import re
import sys
import inflect



def main():
    birthdate=input("birthDate : ")
    
    minutes=Date_manipulator(birthdate)
    p=inflect.engine()
    minutes=p.number_to_words(minutes, andword="")
    print(minutes.capitalize() + " minutes")
    
def Date_manipulator(birthdate):
    if re.search("^[0-9]{4}-[0-9]{2}-[0-9]{2}$",birthdate):
        birthyear=int(birthdate[0]+birthdate[1]+birthdate[2]+birthdate[3])
        birthmonth=int(birthdate[5]+birthdate[6])
        birthday=int(birthdate[8]+birthdate[9])
    else:
        sys.exit("Invalid date")

    Birth=date(birthyear,birthmonth,birthday)
    Current=date.today()
    Diff=str(Current-Birth)
    splt=Diff.split("day")
    if splt[0]=="0:00:00":
        days=0
    else:
        days=int(splt[0])

    minutes=days*24*60
    return minutes




if __name__ == "__main__":
    main()

